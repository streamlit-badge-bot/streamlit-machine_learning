import os
import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd
import time
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array, load_img, ImageDataGenerator

def main():
    set_standard_things()
    df_labels = create_dataframe()
    img_label = df_labels.breed
    img_label = pd.get_dummies(df_labels.breed)
    # img_label.head()
    model = load_transfer_model()
    
    st.write('We are working with the following data.')
    st.dataframe(df_labels.head(3)) # this allow for more specific options
    
    st.write('adding filepatch to dataframe')
    df_labels['filename'] = df_labels.id.map(lambda id: f'input/data/train/{id}.jpg')
    st.dataframe(df_labels.head(3))
    
    st.write('Data exploration')
    gr_labels = df_labels.groupby("breed").count()
    gr_labels = gr_labels.rename(columns = {"id" : "count"})
    gr_labels = gr_labels.sort_values("count", ascending=False)
    
    st.write('Show the top-10 breed that has the most images')
    gr_labels[:10]
    
    st.write('Data exploration')
    st.bar_chart(df_labels.breed.unique()[:10], use_container_width=True)
    
    # Select a file
    if st.checkbox('Select a file in current directory'):
        folder_path = '.'
        if st.checkbox('Change directory'):
            folder_path = st.text_input('Enter folder path', '.')
        filename = file_selector(folder_path=folder_path)
        st.write('You selected `%s`' % filename)
        st.image(filename)

     # Read in image file
    image = tf.io.read_file(filename)
    # Turn the jpeg image into numerical Tensor with 3 colour channels (Red, Green, Blue)
    image = tf.image.decode_jpeg(image, channels=3)
    # Convert the colour channel values from 0-225 values to 0-1 values
    image = tf.image.convert_image_dtype(image, tf.float32)
    # Resize the image to our desired size (224, 244)
    image = tf.image.resize(image, size=(224, 224))
    new_image = np.expand_dims(image, axis=0)

    yhat = model.predict(new_image)
    label = img_label.columns[np.argmax(yhat)]
    
    label
    'Probability prediction: ', np.max(yhat[0])
    
    
    
    
    
    

#@st.cache
def load_transfer_model():
    return tf.keras.models.load_model('saved_model/my_model')
   
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)
    
def create_dataframe() -> pd.DataFrame:
    return pd.read_csv("input/labels.csv")
    
def set_standard_things():
    st.title('Dog breed classification')
    seed = 42

if __name__ == '__main__':
    main()
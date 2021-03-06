# Streamlit Machine Learning [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/fskroes/streamlit-machine_learning/streamlit-demo.py)


## The dataset
The dataset that is used is from Kaggle.com (https://www.kaggle.com/c/dog-breed-identification/overview). Each image has his own unique ID with the corresponding dog breed. It consists of a collection of 10,000+ labelled images of 120 different dog breeds.

Who's a good dog? Who likes ear scratches? Well, it seems those fancy deep neural networks don't have all the answers. However, maybe they can answer that ubiquitous question we all ask when meeting a four-legged stranger: what kind of good pup is that?

The original ImageNet set has quite a few different dog classes so we can reuse CNNs with pretrained ImageNet weights. With that model as a base layer, we applied some Transfer Learning by added a new layer and make this CNN learn different dog breeds on this dataset.

## So.. what is Streamlit?
With Streamlit https://www.streamlit.io/ Turn data scripts into sharable web apps in minutes. All in Python. All for free. No front-end experience required. Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

## This project
With this Github project I want to demo how you can use a Machine learning model with Streamlit and show quick results. You can look at the code to see examples on how to plot charts or how to upload an image for classification. This example also shows how to load pre-trained model from TensorFlow Hub. For more information, please go to the official documentation of Streamlit.

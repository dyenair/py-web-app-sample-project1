import streamlit as st
from PIL import Image

# start camera
image = st.camera_input("Camera")
# print(image)

if image is not None:
    # create a pillow image instance
    img = Image.open(image)

    # convert the image
    gray_img = img.convert('L')

    # show image
    st.image(gray_img)
import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

# checks if there's an image
if camera_image:

    # create a pillow (PIL) image instance
    img = Image.open(camera_image)

    # convert the pillow (PIL) image to grayscale
    gray_img = img.convert("L")

    # render the grayscale image on the webpage
    st.image(gray_img)


if uploaded_image:
    # create a pillow (PIL) image instance
    img2 = Image.open(uploaded_image)

    # convert the pillow (PIL) image to grayscale
    gray_img2 = img2.convert("L")

    # render the grayscale image on the webpage
    st.image(gray_img2)

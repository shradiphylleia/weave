import streamlit as st
from PIL import Image, ImageEnhance
from streamlit_drawable_canvas import st_canvas
import io

st.subheader('edit and style images of your product✉️')

uploaded_img = st.file_uploader(
    label=' ',
    help='upload image from your device to edit',
    type=['jpg', 'jpeg', 'png']
)

if uploaded_img:
    img = Image.open(uploaded_img).convert('RGB')

    st.sidebar.header('Editing tools')
    brightness = st.sidebar.slider('Brightness', 0.0, 2.0, 1.0)
    contrast = st.sidebar.slider('Contrast', 0.0, 2.0, 1.0)
    colour = st.sidebar.slider('Grading', 0.0, 2.0, 1.0)

    edited = ImageEnhance.Brightness(img).enhance(brightness)
    edited = ImageEnhance.Contrast(edited).enhance(contrast)
    edited = ImageEnhance.Color(edited).enhance(colour).convert("RGBA")

    st.markdown('Edited Image')
    st.image(edited, caption='Preview')


    buf = io.BytesIO()
    edited.save(buf, format="PNG")
    st.download_button(
            'Download image',
            data=buf.getvalue(),
            file_name="edited_image.png",
            mime="image/png"
        )
else:
    st.info("upload product image to start editing")

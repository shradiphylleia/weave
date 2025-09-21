import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import io

st.title('Illustrate here 🖌️')

# Sidebar tools
drawing_mode = st.sidebar.selectbox('Drawing tool:', ('freedraw', 'line'))
width = st.sidebar.slider('Brush thickness:', 1, 15, 3)
stroke_color = st.sidebar.color_picker('Pick brush color:', "#000000")
update = st.sidebar.checkbox('See live result', True)

uploaded_img = st.file_uploader(
    label='Upload an image',
    type=['jpg', 'jpeg', 'png']
)

if uploaded_img:
    st.subheader('draw here:')
    img = Image.open(uploaded_img).convert('RGBA')
    img_resized = img.resize((400, 400))

    canvas_img = st_canvas(
        stroke_width=width,
        stroke_color=stroke_color,
        background_color="",
        update_streamlit=update,
        height=500,
        width=500,
        drawing_mode=drawing_mode,
        display_toolbar=st.sidebar.checkbox('Illustration toolbox', True),
        key='editing_canvas'
    )


    if canvas_img.image_data is not None:
        overlay = Image.fromarray(canvas_img.image_data.astype("uint8"), mode="RGBA")
        overlay = overlay.resize((500, 500))

        combined = img_resized.copy()
        combined.alpha_composite(overlay)

        st.markdown('Final Preview')
        st.image(combined, caption="Image with Illustration")

        buf = io.BytesIO()
        combined.save(buf, format="PNG")
        st.download_button(
            'Download image',
            data=buf.getvalue(),
            file_name="illustrated_image.png",
            mime="image/png"
        )

else:
    st.info('Upload an image to start illustrating.')

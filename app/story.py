import streamlit as st
import requests
import base64

st.set_page_config(layout="wide")
st.subheader('Craft Your Stories Here 📮')

col1, col2 = st.columns([1, 1])

with col1:
    region = st.selectbox(
        label='Enter region you belong to',
        options=[
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
            "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
            "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
            "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
            "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
            "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
        ],
        help='Choose your State or UT',
        key='region_select'
    )

with col2:
    product = st.text_input(
        label='Enter the product you wish to market',
        help='Enter the name of your product, the more descriptive the better',
        placeholder='Handcrafted Himachali Shawl',
        key='product_input'
    )

event = st.text_area(
    label='What happened this week at your workshop',
    help='Enter what you wish to in your placeholder, AI helps build the marketing copy',
    placeholder='We finished a batch of shawls made from pure merino wool, dyed with natural colors derived from local plants. Each piece is unique and tells a story.',
    key='event_input'
)

uploaded_image = st.file_uploader(
    "Upload a product image from the week (optional)",
    type=["png", "jpg", "jpeg"],
    key='image_uploader'
)

st.text(" ") 

if st.button('Generate Marketing Copy', use_container_width=True, type='primary'):
    if not product or not event:
        st.error("Please fill out both the product and event fields.")
    else:
        st.subheader("Generated Marketing Copy:")
        with st.spinner("Generating your personalized marketing copy..."):
            try:
                # data to FastAPI
                payload = {
                    "region": region,
                    "product": product,
                    "event": event
                }
                
                # encode the image to base64 if uploaded
                if uploaded_image:
                    image_bytes = uploaded_image.getvalue()
                    encoded_image = base64.b64encode(image_bytes).decode('utf-8')
                    payload["image"] = encoded_image

                # request to the backend
                response = requests.post(
                    "http://127.0.0.1:8000/generate-copy/",
                    json=payload
                )
                
                if response.status_code == 200:
                    result = response.json()
                    copy_text = result.get("copy", "Could not generate copy.")
                    st.success("Successfully generated!")
                    st.markdown(f"**__{copy_text}__**")
                else:
                    st.error(f"Error from server: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error(
                    "Connection Error: Please make sure your FastAPI server is running."
                )
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

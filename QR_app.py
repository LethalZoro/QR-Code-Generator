import streamlit as st
import qrcode
from PIL import Image
import io

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🎨",
    layout="centered",
)

# --- STATE MANAGEMENT ---
# Initialize session state variables if they don't exist
# We will now store the image as bytes
if 'qr_image_bytes' not in st.session_state:
    st.session_state.qr_image_bytes = None
if 'input_url' not in st.session_state:
    st.session_state.input_url = ""

# --- HELPER FUNCTION ---
def generate_qr_code(url, box_size, border, fill_color, back_color):
    """Generates a QR code image and returns it as a PIL Image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def image_to_bytes(img):
    """Converts a PIL Image to a byte array for display and download."""
    # As you correctly pointed out, we use BytesIO to handle the binary data
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

# --- UI LAYOUT ---

# Title and Subtitle
st.title('✨ QR Code Generator')
st.markdown("Create stylish, custom QR codes with ease. Enter a URL, tweak the design, and download your creation!")

st.divider()

# Create two columns: one for controls, one for the QR code display
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🛠️ Customization")

    # URL Input
    url = st.text_input("Enter the URL:", placeholder="e.g., https://www.google.com", key="input_url")

    # Advanced options in an expander
    with st.expander("🎨 Advanced Options"):
        fill_color = st.color_picker('Foreground Color', '#000000')
        back_color = st.color_picker('Background Color', '#FFFFFF')
        box_size = st.slider('Box Size (Pixel size of each QR code box)', 5, 20, 10, 1)
        border = st.slider('Border Size (Thickness of the border)', 1, 10, 4, 1)

    # Generate Button
    if st.button('🚀 Generate QR Code', use_container_width=True, type="primary"):
        if url:
            with st.spinner('Generating your masterpiece...'):
                # Generate the PIL Image
                img = generate_qr_code(url, box_size, border, fill_color, back_color)
                
                # CORRECTED STEP: Convert the image to bytes
                img_bytes = image_to_bytes(img)
                
                # Store the bytes in session state
                st.session_state.qr_image_bytes = img_bytes
        else:
            st.warning('Please enter a URL to generate a QR code.')

with col2:
    st.subheader("🖼️ Preview")
    
    # Check if the image bytes exist in session state
    if st.session_state.qr_image_bytes:
        # Display the generated QR code from session state bytes
        st.image(st.session_state.qr_image_bytes)
        
        # Native Streamlit Download Button now uses the same bytes
        st.download_button(
            label="📥 Download QR Code",
            data=st.session_state.qr_image_bytes,
            file_name=f"qr_code_for_{st.session_state.input_url.replace('https://', '').replace('http://', '').split('/')[0]}.png",
            mime="image/png",
            use_container_width=True,
        )
    else:
        # Placeholder or instruction
        st.info("Your generated QR code will appear here.")

# --- FOOTER ---
st.markdown("---")
st.markdown('Made with ❤️ by a [Salik Labs Developer](https://www.saliklabs.com/)')
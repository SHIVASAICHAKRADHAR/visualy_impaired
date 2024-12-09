import streamlit as st
import google.generativeai as genai
from PIL import Image
from langchain_google_genai import GoogleGenerativeAI
import os
from gtts import gTTS

######################
st.snow()
st.title("🚀 🤖 AI Powered Solution for Assisting Visually Impaired Individuals 🖼️ 📝")
######################

genai.configure(api_key = key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=key)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        font-weight: 800;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555;
    }
    .feature-header {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    footer {
        text-align: center;
        color: #aaa;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown('<div class="subtitle">AI-Powered Assistance for Visually Impaired Individuals</div>', unsafe_allow_html=True)

# Sidebar with Features and Instructions
st.sidebar.markdown(
    """
    ### Features:
    - 👩🏻‍🏫 **Describe Scene**: Describe the image in detailed using AI.
    - 🔍 **Detect the Scene in depth**: Detect Objects and Obstacles within the image.
    - 🔊 **Text-to-Speech**: Listen to the text based on which feature user selected.
    - 👩🏻‍💼 **Personalized Assistance**: identify items or objects and text available on the image to read and display.
    - 📋 **Get Tasks**: Get tasks based on given image location.
    
    ### How It Works:
    1. Upload an image.
    2. Select a feature to interact with the AI.
    """
)

st.sidebar.success("Upload an image to start!")

# Functions
def task(prompt, image_data):
    """Generates tasks based on image using Google Generative AI."""
    response = model.generate_content([prompt, image_data[0]])
    return response.text

def assistance(prompt, data):
    """Identify items or objects and text or labels from image using Google Generative AI."""
    input_text = f"{prompt}\nExtracted text: {data}"
    response = llm.generate(prompts=[input_text])
    if response.generations and len(response.generations[0]) > 0:
        data = response.generations[0][0].text
        return data

def text_to_speech(text):
    """Function to convert text to speech and save it as a file"""
    audio_file = "output_1.mp3"
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(audio_file)
    return audio_file

def detect(prompt, image_data):
    """Detects Objects and Obstacles from scene using Google Generative AI."""
    response = model.generate_content([prompt, image_data[0]])
    return response.text

def describe(prompt, image_data):
    """Generates a scene description using Google Generative AI."""
    res = model.generate_content([prompt, image_data[0]])
    return res.text

def prepare_image_data(uploaded_file):
    """Prepares uploaded image for API processing."""
    if uploaded_file:
        return [
            {
                "mime_type": uploaded_file.type,
                "data": uploaded_file.getvalue(),
            }
        ]
    else:
        raise ValueError("No file uploaded.")

# Main Section
uploaded_file = st.file_uploader("Drag and drop or browse an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.markdown("<h3 class='feature-header'>⚙️ Features</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("👩🏻‍🏫 Illustrate"):
        with st.spinner("Analyzing the scene..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = describe(
                    "Describe the scene in the uploaded image in detail, offering insights to enhance user thoughts.", image_data
                    )
                text = f"Describe the Scene: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>👩🏻‍🏫 Scene Description</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    if col2.button("🔍 Detect"):
        with st.spinner("Detecting the scene in depth..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = detect(
                    "Identify objects and obstacles within the image and highlight them, offering insights to enhance user safety and situational awareness.", image_data
                    )
                text = f"Detecting the Scene in depth: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>🔍 Detecting the Scene for any objects and obstacles</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    if col3.button("👩🏻‍💼 PA"):
        with st.spinner("Working on the scene..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                data = describe(
                    "Describe the scene in the uploaded image in detail, offering insights to enhance user thoughts.", image_data
                    )
                prompt = f"Identifying Items, text and display them."
                response = assistance(prompt, data)
                text = f"Acts as Personalized Assistance: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>👩🏻‍💼 Personalized Assistance</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    if col4.button("📋 Tasks"):
        with st.spinner("Analyzing the scene for tasks..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = task(
                    "Suggest best and top 10 tasks a user can do based on the location of the image scene.", image_data
                    )
                text = f"Suggesting the few tasks user can do based on given image scene: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>📋 Tasks based on scene</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer with a user-friendly message
st.markdown(
    """
    <footer>
        Powered by <strong>Google Gemini API</strong> | Created for Accessibility | Built with ❤️ using Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)

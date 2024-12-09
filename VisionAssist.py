import streamlit as st
import google.generativeai as genai
from PIL import Image
from langchain_google_genai import GoogleGenerativeAI
import os
from gtts import gTTS


st.balloons()
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #0044cc; /* Blue color */
            background-color: #f0f0f0; /* Light grey background */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
    </style>
    <div class="title">
        🌟 Empowering Vision: Chakradhar's AI-Driven Solution for Visually Impaired Assistance 🤖 📝
    </div>
""", unsafe_allow_html=True )


genai.configure(api_key = "AIzaSyAzV9EjQbrPEKFuxMYfWv-k9sWkHf0USwk")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key = "AIzaSyAzV9EjQbrPEKFuxMYfWv-k9sWkHf0USwk")

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
st.markdown("""
    <style>
        .subtitle {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff; /* White color for text */
            background: linear-gradient(45deg, #00BFAE, #0077B6); /* Green to Blue */
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
    </style>
    <div class="subtitle">
        🌐 AI-Powered Solutions for Empowering Visually Impaired Individuals 🤖
    </div>
""", unsafe_allow_html=True)


# Sidebar with Features and Instructions
st.markdown("""
    <style>
        .sidebar-box {
            background: linear-gradient(45deg, #6a5acd, #8a2be2); /* Gradient background (blue to purple) */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            color: #ffffff;
            margin-bottom: 20px;
        }
        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 12px;
        }
        .sidebar-text {
            font-size: 16px;
            color: #f1f1f1;
            line-height: 1.6;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        .sidebar-text strong {
            color: #ffcc00; /* Golden color for bold items */
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content with a box and shaded background
st.sidebar.markdown("""
    <div class="sidebar-box">
        <div class="sidebar-title">🚀 Key Features</div>
        <div class="sidebar-text">
            <ul>
                <li>🖼️ <strong>Scene Description</strong>: Provides a comprehensive AI-generated description of the uploaded image.</li>
                <li>🔍 <strong>Advanced Scene Detection</strong>: Identifies key objects and obstacles within the image.</li>
                <li>🎧 <strong>Text-to-Speech</strong>: Converts the selected text into speech for a hands-free experience.</li>
                <li>📝 <strong>Personalized Assistance</strong>: Detects and reads out items, objects, and text within the image.</li>
                <li>📌 <strong>Task Recommendations</strong>: Suggests relevant tasks based on the context and location of the image.</li>
            </ul>
        </div>
        <div class="sidebar-title">🛠️ How It Works</div>
        <div class="sidebar-text">
            1. Upload your image.<br>
            2. Choose a feature to interact with and receive assistance from the AI.<br>
        </div>
    </div>
""", unsafe_allow_html=True)




st.sidebar.success("**Upload an image to start!**")

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
uploaded_file = st.file_uploader("Drag and drop or browse an image (JPG, JPEG, PNG,HEIC)", type=["jpg", "jpeg", "png", "heic"])

st.snow()
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.markdown("<h3 class='feature-header'> 🚂 Features </h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("👩🏻‍🏫 **Illustrate**"):
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
        Made by <strong> Shiva Sai Chakradhar </strong> | Created for Accessibility | Built with 💝 for Visual Impaired 🧍🏻
    </footer>
    """,
    unsafe_allow_html=True,
)

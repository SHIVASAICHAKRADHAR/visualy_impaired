import streamlit as st
import google.generativeai as genai
from PIL import Image
from langchain_google_genai import GoogleGenerativeAI
import os
from gtts import gTTS


######################
st.snow()
st.title("🌟 Accessible AI for Visually Impaired Individuals 🚀")

# Reading the API Key and Configuring the API Key

genai.configure(api_key="AIzaSyAzV9EjQbrPEKFuxMYfWv-k9sWkHf0USwk")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAzV9EjQbrPEKFuxMYfWv-k9sWkHf0USwk")

st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        font-weight: 800;
        text-align: center;
        color: #FFD700;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #4CAF50;
    }
    .feature-header {
        font-size: 28px;
        font-weight: bold;
        color: #333;
    }
    .footer-text {
        text-align: center;
        color: #888;
        font-size: 16px;
    }
    .description-text {
        font-size: 18px;
        color: #333;
        line-height: 1.5;
    }
    .feature-button {
        background-color: #4CAF50;
        color: white;
        padding: 15px;
        border-radius: 5px;
        font-size: 18px;
        margin: 10px;
    }
    .feature-button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown('<div class="subtitle">Empowering Visually Impaired with AI Assistance</div>', unsafe_allow_html=True)


# Sidebar with Features and Instructions
st.sidebar.image(
    r"Pics/vision_img.jpg",
    width=200,
)

st.sidebar.markdown(
    """
    ### How This Works:
    - 🚶‍♀️ **Describe Scene**: Get a detailed description of your surroundings.
    - 🛑 **Detect Objects**: Identify obstacles or important items in your environment.
    - 🔊 **Text-to-Speech**: Listen to AI descriptions and details about your surroundings.
    - 🧑‍💼 **Personal Assistance**: Recognize text and objects for everyday help.
    - 📝 **Suggested Tasks**: Get suggested tasks based on your current environment.
    
    ### Steps to Use:
    1. Upload an image of your surroundings.
    2. Choose a feature to start interacting with the AI.
    3. Listen to the audio feedback or read the descriptions.
    """
)

st.sidebar.success("Upload an image to start your experience!")


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
uploaded_file = st.file_uploader("Please upload an image of your surroundings (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.markdown("<h3 class='feature-header'>✨ AI Features to Enhance Your Experience</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("🖼️ Describe Scene", key="1"):
        with st.spinner("Analyzing the scene..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = describe(
                    "Describe the scene in the uploaded image in detail to guide the user with their surroundings.", image_data
                )
                text = f"Scene Description: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>🖼️ Scene Description</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")


    if col2.button("🛑 Detect Obstacles", key="2"):
        with st.spinner("Detecting objects and obstacles..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = detect(
                    "Identify obstacles or objects in the image and highlight them for better awareness and safety.", image_data
                )
                text = f"Obstacle Detection: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>🛑 Detect Obstacles</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")


    if col3.button("🧑‍💼 Personalized Assistance", key="3"):
        with st.spinner("Identifying objects and labels..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                data = describe(
                    "Describe the scene in the uploaded image in detail, offering insights for better user understanding.", image_data
                )
                prompt = f"Identify objects, text, and offer personalized assistance based on the image."
                response = assistance(prompt, data)
                text = f"Personalized Assistance: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>🧑‍💼 Personalized Assistance</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")


    if col4.button("📝 Suggested Tasks", key="4"):
        with st.spinner("Analyzing tasks based on the scene..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = task(
                    "Suggest relevant tasks based on the environment and location visible in the image.", image_data
                )
                text = f"Suggested Tasks: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>📝 Suggested Tasks</h3>", unsafe_allow_html=True)
                st.write(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")


# Footer
st.markdown(
    """
    <footer class="footer-text">
        Empowering You with AI-Driven Assistance | Created with Care Using Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)

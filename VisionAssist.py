import streamlit as st
import google.generativeai as genai
from PIL import Image
from langchain_google_genai import GoogleGenerativeAI
import os
from gtts import gTTS


st.markdown("""
    <script>
        // Falling leaves and flowers effect
        const createFallingElement = (type) => {
            let element = document.createElement('div');
            element.style.position = 'absolute';
            element.style.left = `${Math.random() * window.innerWidth}px`;
            element.style.animation = `falling ${Math.random() * 5 + 3}s linear infinite, sway ${Math.random() * 4 + 3}s ease-in-out infinite`;
            element.style.zIndex = '9999';
            element.style.pointerEvents = 'none';
            element.style.transition = 'all 0.5s ease-in-out';
            
            // Choose the image for falling leaves or flowers
            if (type === 'leaf') {
                element.style.backgroundImage = 'url("https://img.icons8.com/ios/452/leaf.png")';
                element.style.width = '30px';
                element.style.height = '30px';
                element.style.backgroundSize = 'contain';
            } else if (type === 'flower') {
                element.style.backgroundImage = 'url("https://img.icons8.com/ios/452/flower.png")';
                element.style.width = '25px';
                element.style.height = '25px';
                element.style.backgroundSize = 'contain';
            }
            document.body.appendChild(element);
            
            setTimeout(() => {
                document.body.removeChild(element);
            }, 7000); // Remove element after it finishes falling
        };

        // Generate falling elements (leaves and flowers)
        setInterval(() => {
            if (Math.random() < 0.5) {
                createFallingElement('leaf');
            } else {
                createFallingElement('flower');
            }
        }, 500);

        // CSS animations for falling and swaying effect
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes falling {
                0% { top: -50px; opacity: 1; }
                100% { top: 100vh; opacity: 0; }
            }

            @keyframes sway {
                0% { transform: translateX(0) rotate(0deg); }
                50% { transform: translateX(50px) rotate(10deg); }
                100% { transform: translateX(0) rotate(0deg); }
            }
        `;
        document.head.appendChild(style);
    </script>
""", unsafe_allow_html=True)


#title with white background

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



st.markdown("""
    <style>
        .success-message {
            background-color: #4CAF50; /* Green background */
            color: white;
            padding: 15px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)


# Apply the custom styling to the success message
st.sidebar.markdown('<div class="success-message">  <strong>Upload an Image to View </strong> </div>', unsafe_allow_html=True)


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
    """Function to convert text to speech and save it as a file."""
    # Remove any colons from the text
    cleaned_text = text.replace(":", "")
    
    # Convert the cleaned text to speech
    audio_file = "output_1.mp3"
    tts = gTTS(text=cleaned_text, lang="en", slow=False)
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
st.markdown("""
    <style>
        .feature-header {
            font-size: 20px;
            color: #4CAF50;
            text-align: center;
            margin-top: 10px;
        }
        .button-style {
            background-color: #FF9800;  /* Button Color - Orange */
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
            width: 100%;
            border: none;
            cursor: pointer;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .button-style:hover {
            background-color: #F57C00;  /* Darker orange on hover */
        }
    </style>
""", unsafe_allow_html=True)

# File upload section
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.markdown("<h3 class='feature-header'> 🚂 Features </h3>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # Box for Scene Description
    if col1.button("🖼️ **Illustrate Scene**", key="1", help="Describe the scene in detail and offer insights"):
        with st.spinner("Analyzing the scene..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = describe(
                    "Describe the scene in the uploaded image in detail, offering insights to enhance user thoughts", image_data
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

    # Box for Scene Detection
    if col2.button("🔍 **Detect Scene**", key="2", help="Detect objects and obstacles in the image"):
        with st.spinner("Detecting the scene in depth..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = detect(
                    "Identify objects and obstacles within the image and highlight them, offering insights to enhance user safety and situational awareness", image_data
                )
                text = f"Detecting the Scene: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>🔍 Detecting the Scene</h3>", unsafe_allow_html=True)
                st.write(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # Box for Personalized Assistance
    if col3.button("🧑🏻‍💼 **Personalized Assistance**", key="3", help="Identify items and text in the image"):
        with st.spinner("Working on the scene..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                data = describe(
                    "Describe the scene in the uploaded image in detail, offering insights to enhance user thoughts", image_data
                )
                prompt = "Identifying items and text within the image."
                response = assistance(prompt, data)
                text = f"Personalized Assistance: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>🧑🏻‍💼 Personalized Assistance</h3>", unsafe_allow_html=True)
                st.write(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # Box for Task Suggestions
    if col4.button("📝 **Task Suggestions**", key="4", help="Suggest tasks based on the image context"):
        with st.spinner("Analyzing tasks..."):
            try:
                image_data = prepare_image_data(uploaded_file)
                response = task(
                    "Suggest the best tasks a user can do based on the location of the image scene", image_data
                )
                text = f"Task Suggestions: {response}"
                audio_file = text_to_speech(text)
                with open(audio_file, "rb") as file:
                    st.audio(file.read(), format="audio/mp3")
                os.remove(audio_file)
                st.markdown("<h3 class='feature-header'>📝 Suggested Tasks</h3>", unsafe_allow_html=True)
                st.write(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")



st.markdown(
    """
    <style>
        footer {
            background: linear-gradient(45deg, #ff6ec7, #ffc3a0, #ff9a8b, #ff6a00);
            padding: 20px;
            font-size: 24px;
            color: white;
            text-align: center;
            border-radius: 15px;
            animation: color-change 5s infinite alternate;
        }

        @keyframes color-change {
            0% {
                background: #ff6ec7;
            }
            25% {
                background: #ffc3a0;
            }
            50% {
                background: #ff9a8b;
            }
            75% {
                background: #ff6a00;
            }
            100% {
                background: #ff6ec7;
            }
        }
    </style>
    <footer>
        Made by <strong>Shiva Sai Chakradhar</strong> | Created for Accessibility | Built with 💝 for Visual Impaired 🧍🏻
    </footer>
    """,
    unsafe_allow_html=True,
)


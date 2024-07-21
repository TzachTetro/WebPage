import streamlit_lottie
from email.mime import image
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Set page configuration
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding_1 = load_lottieurl("https://lottie.host/98d7dfef-42d4-4a6f-b84f-20ced92a02c4/TArknmcRno.json")
lottie_coding_2 = load_lottieurl("https://lottie.host/93c259bf-f0c6-4091-b520-cdf9a4059259/v3d0WTjfqi.json")
img_contact_from_1 = Image.open("images/Cipher_1.png")
img_lottie_animation = Image.open("images/Cipher_2.png")
img_contact_from_2 = Image.open("images/Cipher_3.png")
img_contact_from_3 = Image.open("images/Cipher_4.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("Hi, I am Tzach! 🎗")
    st.header("A Cybersecurity and Software Engineering Student")
    st.write("---")
    text_column, image_column = st.columns([2, 1])  # Adjusted column ratio
    with text_column:
        st.write(
            """
            My journey in software engineering has led me to develop a passion for cybersecurity, and I am now eager to transition into this field. I am particularly interested in roles that focus on network security, vulnerability assessment, and incident response. My background in software engineering provides me with a strong foundation in problem-solving and technical skills, which I am excited to apply to cybersecurity challenges. I am actively seeking opportunities to contribute to and grow within a dynamic team in the cybersecurity industry, where I can leverage my skills and dedication to enhance security measures and protect valuable information.
            """
        )
    with image_column:
        st.image(img_contact_from_1, width=200)  # Set the image width to make it smaller

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me :wave:")
        st.write(
            """
            I am a Software Engineering student at the Open University, studying cybersecurity online. With a strong interest in technology and a dedication to solving complex problems, I am passionate about cybersecurity. My journey has been fueled by a relentless curiosity and a commitment to continuous learning. I thrive on the challenges presented by the ever-evolving landscape of cybersecurity and am driven to stay ahead of the curve. I actively seek out opportunities to apply my knowledge in real-world scenarios and contribute to creating secure digital environments. Beyond academics, I am an avid collaborator and enjoy working with like-minded individuals to innovate and make a positive impact in the field of cybersecurity.
            
        
            """
        )
        st.write("[Watch My Linkedin!](https://www.linkedin.com/in/tzachtetro)")
    with right_column:
        st_lottie(lottie_coding_1, height=300, key="coding1")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Cryptography Cipher Project 💻")
    st.write("#")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with image_column:
        st.image(img_contact_from_2)     
    with text_column:
        st.write(
            """
            This project implements a Caesar Cipher encryption and decryption tool with added features such as support for multiple languages, history tracking, and a reverse cipher option. It is written in Python and includes a simple command-line interface for user interaction. The tool not only encrypts and decrypts text but also provides a robust user experience with intuitive commands and clear outputs. By supporting multiple languages, it caters to a diverse user base, and the history tracking feature allows users to revisit previous encryption and decryption operations effortlessly. The reverse cipher option adds an extra layer of versatility, making this tool a comprehensive solution for various cryptographic needs. This project showcases my skills in Python programming, problem-solving, and my understanding of fundamental cryptographic concepts.
            """
        )
        st.markdown("[Watch my GitHub for More!](https://github.com/TzachTetro/TzachTetro09)")

    
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in Touch with Me!")
    st.write("##")
    
    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/tzachno1@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding_2, height=325, key="coding2")
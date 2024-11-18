import streamlit as st
import random
import time
from PIL import Image

# Create a placeholder for content
placeholder = st.empty()

# Display first content (Random meme)
with placeholder.container():
    st.write("""<h1 style="text-align:center">CTRL + ALT + MEME</h1>""", unsafe_allow_html=True)
    
    meme_images = [
        "https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif",  # Example GIF from GIPHY
        "./memes/meme_1.png",
        "./memes/meme_2.png",
        "./memes/meme_3.png",
        "./memes/meme_4.png",
        "./memes/meme_5.png",
        "./memes/meme_6.png",
        "./memes/meme_7.png",
        "./memes/meme_8.png",
        "./memes/meme_10.png",
        "./memes/meme_11.png",
        "./memes/meme_12.png",
        "./memes/meme_13.png",
        "./memes/meme_14.png",
        "./memes/meme_15.png"
    ]
    
    # Select a random image from the list
    random_image = random.choice(meme_images)
    
    # If it's a URL, display it as a GIF or an image
    if random_image.startswith("http"):
        st.image(random_image, width=700)
    else:
        image = Image.open(random_image)
        st.image(image, width=700)
    
    time.sleep(5)  # Wait for 2 seconds

# Clear the placeholder content
placeholder.empty()

# Swap to second content (text change)
with placeholder.container():
    st.write("""<h1 style="text-align:center">We know what you need and here you go!</h1>""", unsafe_allow_html=True)


    st.markdown("""
        <h4>Resources</h4>
        <ol>
            <li>
                <a href="https://github.com/AbhishekDGoudar/Job-Skills-Recommendations" target="_blank">
                    Click here to view the GitHub repository
                </a>
            </li>
            <li>
                <a href="https://mavsuta-my.sharepoint.com/:u:/g/personal/txk4530_mavs_uta_edu/EbnaVh-VbwNEsqbXORImvKkBfW3uxnX3qfVzYt0c4DWBLw?e=opEbE2" target="_blank">
                    Click here to view the Power BI Visualization
                </a>
            </li>
        </ol>
    """, unsafe_allow_html=True)
import streamlit as st 
from transformers import pipeline
from PIL import Image
import io
from streamlit_option_menu import option_menu

st.set_page_config(page_title="rostaing.ai | ai-app", page_icon="logo/Logo_RostaingAI.jpeg")

with st.sidebar:
    
    seleted = option_menu(
        "MENU",
        ["Sentiment analysis", "Image to text"],
        icons = ["chat-text", "card-image"],
        menu_icon = "cast",
        default_index = 0     
    )
    
def sentiment_analysis():
    classifier = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    message = st.text_input("Message")

    if st.button("Apply"):
        st.divider()
        st.write("", classifier(message))
        st.balloons()
        st.divider() 


def imaga_text():
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    image = st.file_uploader("Upload an image.")

    # Afficher l'image si elle a été téléchargée avec succès
    if image is not None:
        st.image(image)

        # Convertir l'objet BytesIO en une image PIL
        image_pil = Image.open(io.BytesIO(image.read()))

        # Passer l'image PIL à la fonction image_to_text
        text_from_image = image_to_text(image_pil)

        # Afficher le texte extrait de l'image
        st.write(text_from_image)
        st.balloons()  
    else:
        st.write("Please upload an image.")
    # [{'generated_text': 'a soccer game with a player jumping to catch the ball '}]
 
def main():
    if seleted == "Sentiment analysis":
        sentiment_analysis()
    elif seleted == "Image to text":
        imaga_text()

if __name__ == "__main__":
    main()


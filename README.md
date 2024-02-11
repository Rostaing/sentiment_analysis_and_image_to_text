This project is a Streamlit application that utilizes the Hugging Face Transformers library to perform two different tasks based on user choice:

1. **Sentiment Analysis**: Users can input a message into a text field and click a button to apply sentiment analysis to that message. The application uses the "distilbert-base-uncased-finetuned-sst-2-english" model to perform this task. Once the analysis is done, the results are displayed to the user, with the option to view the result in a message balloon.

2. **Image to Text Conversion**: Users can upload an image from their file system. The application then displays the uploaded image and uses the "vit-gpt2-image-captioning" model to extract text from the image. Once the text is extracted, it is displayed to the user, with the option to view it in a message balloon.

The user interface is managed using Streamlit, with a sidebar allowing users to choose between the two available functionalities. The `streamlit_option_menu` library is used to create a dropdown menu with selectable options and icons for each option.

In summary, this application provides a user-friendly interface for performing two different AI tasks: sentiment analysis on text and text extraction from images.

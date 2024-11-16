# import streamlit as st
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# model = "ahmedshark/shark-finetuned-kde4-ar-en"  # Replace with your model's path
# model = AutoModelForSeq2SeqLM.from_pretrained(model)
# tokenizer = AutoTokenizer.from_pretrained(model)

# st.title("Translation App")
# st.write("Enter text to translate:")

# # Input text
# input_text = st.text_area("Input Text")

# # Translate button
# if st.button("Translate"):
#     if input_text:
#         # Prepare the input for the model
#         inputs = tokenizer(input_text, return_tensors="pt")
        
#         # Generate translation
#         outputs = model.generate(**inputs)
#         translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
#         # Display the result
#         st.write("Translation:")
#         st.success(translation)
#     else:
#         st.warning("Please enter text to translate.")


import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load model and tokenizer
model_path = "ahmedshark/shark-finetuned-kde4-ar-en"  # Replace with your model's path
try:
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    st.write(f"Model loaded from {model_path}")
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None
    tokenizer = None

# Check if model and tokenizer are loaded
if model and tokenizer:
    st.title("Translation App")
    st.write("Enter text to translate:")

    # Input text
    input_text = st.text_area("Input Text")

    # Translate button
    if st.button("Translate"):
        if input_text:
            try:
                # Prepare the input for the model
                inputs = tokenizer(input_text, return_tensors="pt")

                # Check for GPU availability
                device = "cuda" if torch.cuda.is_available() else "cpu"
                model = model.to(device)
                inputs = {key: value.to(device) for key, value in inputs.items()}

                # Generate translation
                outputs = model.generate(**inputs)
                translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

                # Display the result
                st.write("Translation:")
                st.success(translation)
            except Exception as e:
                st.error(f"Error during translation: {e}")
        else:
            st.warning("Please enter text to translate.")
else:
    st.warning("Model and tokenizer are not loaded properly.")

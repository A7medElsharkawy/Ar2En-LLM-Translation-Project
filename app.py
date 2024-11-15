import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load model and tokenizer
model_dir = ".\\translation_model"  # Replace with your model's path
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)

st.title("Translation App")
st.write("Enter text to translate:")

# Input text
input_text = st.text_area("Input Text")

# Translate button
if st.button("Translate"):
    if input_text:
        # Prepare the input for the model
        inputs = tokenizer(input_text, return_tensors="pt")
        
        # Generate translation
        outputs = model.generate(**inputs)
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Display the result
        st.write("Translation:")
        st.success(translation)
    else:
        st.warning("Please enter text to translate.")

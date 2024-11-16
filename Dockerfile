# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app
RUN pip install sentencepiece
# Copy the current directory contents into the container at /app
COPY app.py  app.py
COPY requirement.txt  requirement.txt

# Install dependencies
RUN pip install streamlit transformers[sentencespace] torch

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]

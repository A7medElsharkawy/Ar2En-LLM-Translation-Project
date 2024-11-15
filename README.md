# Ar2En-LLM-Translation-Project


This project is a fine-tuned translation model designed to translate Arabic  to English lang. The model is based on a pre-trained model from Hugging Face and has been fine-tuned on the KDE4 dataset, which contains 116,239 translation sentence pairs.

<p align="center">
  <a href="[https://your-video-link.com](https://your-video-link.com](https://github.com/A7medElsharkawy/Ar2En-LLM-Translation-Project/blob/main/model%20Test.mp4)">Watch the demo video</a>
</p>

[![Installation and Usage Badge](https://img.shields.io/badge/Installation--Usage-README-red)](README.md)
[![Project Workflow](https://img.shields.io/badge/PROJECT--WORKFLOW-README-blue)](PROJECT-WORKFLOW.md)

## Project Structure

Here's an overview of the key files and directories:

- **translation_model/**: This directory contains the fine-tuned model.
- **app.py**: A Streamlit application to interact with the model through a user-friendly web interface.
- **Dockerfile**: Defines the environment for deploying the model as a Docker container.
- **model_test.mp4**: A video demonstrating the model in action.
- **requirements.txt**: Lists all the dependencies required to run the model and the Streamlit app.
- **fine-tuning-model.ipynb**: this is the fine-tuned notebook.

## Dataset

The model was fine-tuned on the [KDE4](https://huggingface.co/datasets/kde4) dataset, which includes 116,239 sentence pairs translating from Modern Standard Arabic to Egyptian Arabic.

## Setup and Installation

### Prerequisites

Ensure you have Python and Docker installed.

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/A7medElsharkawy/Ar2en-Translation-Model.git

   cd Ar2en-Translation-Model


2. build and run docker file:

   ```bash
   docker build -it any-name .

   docker run -p 8501:8501 any-name

   go to  http://localhost:8501/


3. (or) use app.py direct:
    ```bash
    streamlit run app.py  
    ```  






This README structure provides a clear description, setup instructions, and usage guidelines.

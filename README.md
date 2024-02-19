# SCRIPT Generator

This project is a Streamlit app for generating blog posts using the Llama-2-7B-Chat-GGML model.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/blog-generator.git
    cd blog-generator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the blog generator:

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Enter the blog topic, number of words, and select the target audience.
3. Click the "Create" button to generate the blog post.
4. The generated blog post will be displayed on the app.

## Dependencies

The project relies on the following dependencies:

- `streamlit`: For creating the web app interface.
- `transformers`: For loading and using the Llama-2-7B-Chat-GGML model.
- `huggingface_hub`: For downloading the model files from the Hugging Face Model Hub.

Install them using:

```bash
pip install streamlit transformers huggingface_hub

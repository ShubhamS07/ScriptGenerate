import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from ctransformers import AutoModelForCausalLM


def getLLamaResponse(input_text, no_words, blog_type):
    llm = AutoModelForCausalLM.from_pretrained(
        "TheBloke/Llama-2-7B-Chat-GGML",
        model_file="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type='llama',
        max_new_tokens=256,
        temperature=0.01
    )
    template = f"write a blog for {blog_type} job profile for a topic {input_text} within {no_words} words"
    prompt = PromptTemplate(input_variables=[input_text, no_words, blog_type], template=template)
    response = llm(prompt.format(type=blog_type, n_words=no_words, text=input_text))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs", page_icon="📝", layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs 📝")

input_text = st.text_input("Enter The Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of words')
with col2:
    blog_type = st.selectbox('Writing the blog for', ('Researcher', 'Developer', 'common people'), index=0)

submit = st.button("Create")

if submit:
    st.write(getLLamaResponse(input_text, no_words, blog_type))

import streamlit as st
import pandas as pd
import openai

# Set up OpenAI API Key
openai.api_key = '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'

def ask_gpt(question, data):
    prompt = f"Based on the following data: {data}, answer the question: {question}"
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response['choices'][0]['message']['content']

st.title('Excel Chatbot')

# File Upload
uploaded_file = st.file_uploader('Upload your Excel file', type=['xlsx'])
if uploaded_file:
    data = pd.read_excel(uploaded_file)
    st.write('Data Preview:', data.head())
    question = st.text_input('Ask a question about the data:')
    if st.button('Get Answer'):
        answer = ask_gpt(question, data.to_dict())
        st.write('Answer:', answer)
# import os
import streamlit as st
# from dotenv import load_dotenv
from langchain_openai import OpenAI

# load_dotenv()

llm = OpenAI()

st.title('수학문제 풀이')
content = st.text_input("수학 문제를 제시해주세요.", "")

if st.button("문제 풀이"):
    with st.spinner('문제 풀이 중...'):
        result = llm.invoke(content + "에 대한 수학 문제를 풀어줘")
        st.write(result)

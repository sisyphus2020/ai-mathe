# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
import time
from langchain_openai import OpenAI

llm = OpenAI()

st.title('수학문제 풀이')
content = st.text_input("수학 문제를 제시해주세요.", "")


result = ''
if st.button("문제 풀이"):
    with st.spinner('문제 풀이 중...'):
        result = llm.invoke(content + "에 대한 수학 문제를 풀어줘")
        st.write(result)

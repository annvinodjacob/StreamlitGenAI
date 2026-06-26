import streamlit as st
from google import genai
from google.genai import types
config=types.GenerateContentConfig(
  system_instructions="""You are an expert in Python programming. Answer all questions asked about Python. Any queries outside Python area, respond as given below.
  "Kindly ask questions about Python Programming Language only".
  """)
st.markdown(
  """
  <h1 style='text-align: center;'> Python AI Assistant</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any Python programming question.
  </p>
  """,
  unsafe_allow_html=True,
)
robo = genai.Client(api_key=st.secrets["MY_GEMINI_API"])
mychat = robo.chats.create(model="gemini-flash-lite-latest")
#Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")
question=config+question
col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Send")

if send:
  response = mychat.send_message(question)
  response_placeholder.write(response.text)

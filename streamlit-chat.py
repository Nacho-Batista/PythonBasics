##APP ANDY

import streamlit as st
import random
import time

st.title("Echo-Bot")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):  #This for loop goes through the chat history and displays the messages.
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("What is up?"): #This is the user input.
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt) #This displays the user message in the chat message container.
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt}) #This adds the user message to the chat history.
    response = f"Echo: {prompt}" 
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


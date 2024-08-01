import requests
import streamlit as st

API_URL = "http://localhost:3000/api/v1/prediction/2ce76a0b-c5e2-40f9-b644-fdb967eefe5c"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

# Show title and description.
st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot that uses Flowise API to generate responses. "
    "To use this app, you need to provide an API key, if applicable."
)

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response using the Flowise API.
    response_data = query({"question": prompt})
    response_content = response_data.get("answer", "Sorry, I couldn't generate a response.")

    # Display the assistant's response.
    with st.chat_message("assistant"):
        st.markdown(response_content)

    # Store the assistant's response in session state.
    st.session_state.messages.append({"role": "assistant", "content": response_content})

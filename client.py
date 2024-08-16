import requests
import streamlit as st

def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }

    try:
        # Send the request
        response = requests.post("https://llm-model-1.onrender.com/chain/invoke", json=json_body)
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        # Parse the JSON response
        result = response.json()
        print("Response JSON:", result)
        # Extract the translated text from the 'output' key
        translated_text = result.get('output', 'No translation found.')
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        translated_text = "Error in translation."

    return translated_text

## Streamlit app
st.title("LLM Application Using LCEL")

# Input fields
language = st.text_input("Enter the language to convert to (e.g., Hindi):")
input_text = st.text_input("Enter the text you want to convert:")

if input_text and language:
    # Get the translated text and display it
    translated_text = get_groq_response(input_text, language)
    st.write(f"Translated Text: {translated_text}")

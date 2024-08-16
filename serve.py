from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch the Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the ChatGroq model
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Create the prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Define the output parser
parser = StrOutputParser()

# Create the chain
chain = prompt_template | model | parser

# Initialize the FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain runnable interfaces"
)

# Add chain routes
add_routes(app, chain, path="/chain")

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

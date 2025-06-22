from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server",
)

# I am assuming you have 'llama3' model available in Ollama.
# If not, please change it to a model you have.
llm = ChatOllama(model="llama3.2:latest")

# Route for essay generation
prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
add_routes(app, prompt | llm, path="/essay")

# Route for direct interaction with the Ollama model
add_routes(app, llm, path="/ollama")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info")

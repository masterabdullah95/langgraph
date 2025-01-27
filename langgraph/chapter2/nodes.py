from classes import State
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

GOOGLE_GEMINI_API_KEY = config('GOOGLE_GEMINI_API_KEY')

llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    api_key=GOOGLE_GEMINI_API_KEY,
    model="gemini-2.0-flash-exp",
)

def node_1(state: State) -> str:
    result = llm.invoke(state["prompt"])
    return {"output": result.content}
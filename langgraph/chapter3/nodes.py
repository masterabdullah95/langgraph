from classes import State
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config
from random import randint

GOOGLE_GEMINI_API_KEY = config('GOOGLE_GEMINI_API_KEY')

llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    api_key=GOOGLE_GEMINI_API_KEY,
    model="gemini-2.0-flash-exp",
)

def node_1(state: State) -> str:
    return {"output": "node1 calling"}
def node_2(state: State) -> str:
    return {"output": "node2 calling"}
def node_3(state: State) -> str:
    return {"output": "node3 calling"}
def conditional_node(state: State) -> str:
    guess = randint(1, 2)
    if guess == 1:
        return "node_two"
    else:
        return "node_three"
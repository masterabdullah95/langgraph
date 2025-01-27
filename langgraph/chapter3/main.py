from langgraph.graph import StateGraph, START, END
from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
from classes import State
from tools import addition, division
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage

GOOGLE_GEMINI_API_KEY = config('GOOGLE_GEMINI_API_KEY')

llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    api_key=GOOGLE_GEMINI_API_KEY,
    model="gemini-2.0-flash-exp",
)
tools = [addition, division]
llm_with_tool = llm.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def node1(state: State):
    return {"messages": [llm_with_tool.invoke(state["messages"])]}

graph_builder.add_node("node_one", node1)
graph_builder.add_edge(START, "node_one")
graph_builder.add_edge("node_one", END)

graph = graph_builder.compile()

res = graph.invoke({"messages": [HumanMessage(content="What is the sum of 1 and 2?")]})
print(res)


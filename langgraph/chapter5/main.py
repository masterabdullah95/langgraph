from langgraph.graph import StateGraph, START, END, MessagesState
from classes import State
from nodes import func_call
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
from tools import addition, division
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

tools = [addition, division]

graph_builder = StateGraph(MessagesState)

graph_builder.add_node("func_call", func_call)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "func_call")
graph_builder.add_conditional_edges("func_call", tools_condition)
graph_builder.add_edge("tools", "func_call")

graph = graph_builder.compile(checkpointer=memory)

sys_msg = SystemMessage(content="Consider you are my assistant and math calculation expert.")
config = {"configurable": {"thread_id": "1"}}

while True:
    query = input("Enter your question: ")
    
    res = graph.invoke({"messages": [sys_msg, HumanMessage(content=query)]}, config)  
    print(res["messages"][-1].content)

    if query == "exit":
        break


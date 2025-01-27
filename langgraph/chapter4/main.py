from langgraph.graph import StateGraph, START, END, MessagesState
from classes import State
from nodes import func_call
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import ToolNode, tools_condition
from tools import tools

graph_builder = StateGraph(MessagesState)

graph_builder.add_node("node_one", func_call)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "node_one")
graph_builder.add_conditional_edges("node_one", tools_condition)
graph_builder.add_edge("tools", END)

graph = graph_builder.compile()

# res = graph.invoke({"messages": [HumanMessage(content="What is the sum of 1 and 2?")]})
# res = graph.invoke({"messages": [HumanMessage(content="10 divided by 2")]})
res = graph.invoke({"messages": [HumanMessage(content="Who is Donald Trump?")]})

for m in res["messages"]:
    print(m.content)


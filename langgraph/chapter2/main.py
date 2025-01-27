from langgraph.graph import StateGraph, START, END

from classes import State
from nodes import node_1, node_2, node_3, conditional_node

graph_builder = StateGraph(State)

graph_builder.add_node("node_one", node_1)
graph_builder.add_node("node_two", node_2)
graph_builder.add_node("node_three", node_3)
graph_builder.add_node("conditional_node", conditional_node)

graph_builder.add_edge(START, "node_one")
graph_builder.add_conditional_edges("node_one", conditional_node)
graph_builder.add_edge("node_two", END)
graph_builder.add_edge("node_three", END)
graph = graph_builder.compile()

res = graph.invoke({"prompt": "Node flow tracking ..."})
print(res)
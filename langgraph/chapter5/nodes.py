from langgraph.graph import MessagesState
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config
from tools import addition, division

GOOGLE_GEMINI_API_KEY = config('GOOGLE_GEMINI_API_KEY')

llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    api_key=GOOGLE_GEMINI_API_KEY,
    model="gemini-2.0-flash-exp",
)
tools = [addition, division]

llm_with_tool = llm.bind_tools(tools)

def func_call(state: MessagesState):
    return {"messages": [llm_with_tool.invoke(state["messages"])]}
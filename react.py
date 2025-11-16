from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_vertexai import ChatVertexAI
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

@tool
def triple(num: float) -> float:
    """
    :param num: a number to triple
    :return: the triple of the input number
    """
    return float(num) * 3

tools = [TavilySearchResults(max_results=1), triple]

llm = ChatVertexAI(
    model="gemini-2.0-flash",
    temperature=0
).bind_tools(tools)
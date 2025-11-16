from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_vertexai import ChatVertexAI
from langchain_tavily import TavilySearchResults

load_dotenv()
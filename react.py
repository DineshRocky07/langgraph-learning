from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def trible (num:float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num)*3

tools = [TavilySearch(max_results=1),trible]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0).bind_tools(tools)

# if __name__ == "__main__":

#     prompt= """can you please trible this number 10"""

#     math_response = llm.invoke(prompt)
#     print("Output AIMessage:")
#     print(f"  Text Content: '{math_response.content}'")
#     print(f"  Tool Calls Requested: {math_response.tool_calls}\n")
#     print("-" * 50)
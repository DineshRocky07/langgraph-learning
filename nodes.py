from dotenv import load_dotenv
from langgraph.graph import MessagesState  #memory
from langgraph.prebuilt import ToolNode   #exceution take last meessage and add to messagestate

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE ="""you are helpfull assistant that can use tools to answer question"""

def run_agent_reasoning_engine(state:MessagesState ) ->MessagesState :
    #state = dictionary
    """run the resoning agen"""
    response =llm.invoke(
        [{"role":"system","content":SYSTEM_MESSAGE}, *state["messages"]]
        
    )

    return {"messages":[response]}

tool_node =ToolNode(tools)


    
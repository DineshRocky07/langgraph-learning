from typing import TypedDict, Annotated
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from chains import generation_chain, reflection_chain

#type dicnory, annotaed metadata, Basemessage all meessge, addmeesasage means applent new messages
class Messagegraph(TypedDict):
     history: Annotated[list[BaseMessage],add_messages]



REFLECT = "reflect"
GENERATE = "generate"

def generation_node(state:Messagegraph):
    return {"history": [generation_chain.invoke({"history": state["history"]})]}
"""Get old history
      ↓
Give it to generation_chain
      ↓
AI creates new response
      ↓
Put response in a list
      ↓
Return {"history": [new response]}"""

def reflection_node(state:Messagegraph):
    res= reflection_chain.invoke({"history": state["history"]})
    print("reflection_node debug",res.content)
    return {"history": [HumanMessage(content=res.content)]}


#scheman stuture data 
builder = StateGraph(state_schema=Messagegraph)
builder.add_node(GENERATE,generation_node)
builder.add_node(REFLECT,reflection_node)
builder.set_entry_point(GENERATE)

def should_conitue(state:Messagegraph):
    if len(state["history"]) > 5:
        return END
    return REFLECT

builder.add_conditional_edges(GENERATE,should_conitue)
builder.add_edge(REFLECT,GENERATE)

graph = builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
# graph.get_graph().print_ascii()

if __name__ == "__main__":
    print("Hello LangGraph!")
    inputs={
        "history":
        [
          HumanMessage(content="Write a tweet about the new features of LangGraph, make it viral and engaging.")
        ]
    }

    response = graph.invoke(inputs)
    print(response)
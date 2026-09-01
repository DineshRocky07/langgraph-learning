from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, START, END

from nodes import run_agent_reasoning_engine,tool_node

AGENT_BRAIN = "agent_brain"
WORKER = "worker"
LAST =-1

flow = StateGraph(MessagesState)

flow.add_node(AGENT_BRAIN,run_agent_reasoning_engine)
flow.set_entry_point(AGENT_BRAIN)
flow.add_node(WORKER,tool_node)

def should_continue(state:dict) -> str:
    if not state["messages"][LAST].tool_calls:
       return END
    return WORKER
flow.add_conditional_edges(
    AGENT_BRAIN,
    should_continue,
    {
        END:END,
        WORKER:WORKER,
    },
)
flow.add_edge(WORKER,AGENT_BRAIN)

app= flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="flown.png")


if __name__=="__main__":
    print("react langgraph agent")

    res= app.invoke(
        {
        "messages":[
            HumanMessage(content="what is the weather in chennai? List it and then trible it ")
        ]
        }
    )
    print(res["messages"][LAST].content)
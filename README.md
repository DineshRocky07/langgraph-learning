# langgraph-learning
Simple guides, tutorials, and code examples for learning LangGraph


1. uv init 
2. we use gemuini
3. agent only run the function @react.py code 

from langgraph.graph import MessageState #memory
from langgraph.prebuild import ToolNode   #exceution take last meessage and add to messagestate this have more feature have
 #state = dictionary

 State (MessagesState): The shared notebook containing the conversation history. Every node reads from it and writes updates back to it.

Nodes (add_node): The workers. Each node is a Python function (like calling the LLM or running tools).

Entry Point (set_entry_point or START): The starting line where execution begins.

Edges (add_edge / add_conditional_edges): The paths connecting the nodes.
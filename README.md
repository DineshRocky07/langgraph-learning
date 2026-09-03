 refection agent 
1.poetry init

chain.py competed 

chainPromptTemplate => prmpt 

messageplaceholder  => empty space to save ans

from_messages => stucture ai give , human give'
 
llm =ChatGoogleGenerativeAI(model="gemini-1.5-flash")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm


main.py
from typing import TypeDict, Annotated -> dicnory give , annotated metadata 

BaseMessage is the common parent/general type.

add_messages → Add messages to state appened new message

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
This is very important in LangGraph.Add the new message to the existing messages.
example :
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]








FYI: wiki usefull:


LLM
↓
The brain

Prompt
↓
Instructions for the brain

Chain
↓
Prompt + LLM connected together

Tool
↓
Something the AI can use/do

Agent
↓
AI decides which tools/actions to use

LangGraph
↓
Controls a complex workflow/loop

Reflection
↓
Generate → Review → Improve
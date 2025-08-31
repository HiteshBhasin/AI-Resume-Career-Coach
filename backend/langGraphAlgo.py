from langgraph.graph import StateGraph
from typing import TypedDict, Annotated, Any, Sequence
from langgraph.graph import END, START, add_messages
from langchain_core.messages import BaseMessage, ToolMessage
from langchain_core.tools import tool

class StateAgent(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    
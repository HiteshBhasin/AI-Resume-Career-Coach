from langgraph.graph import StateGraph
from typing import TypedDict, Annotated, Any, Sequence
from langgraph.graph import END, START, add_messages
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool

class StateAgent(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

system_prompt = SystemMessage(
    content="You are an AI Career Coach. Review resumes and provide constructive, actionable feedback."
)

@tool
def GiveFeedback():
    
    
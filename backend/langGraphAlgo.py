from langgraph.graph import StateGraph
from typing import TypedDict, Annotated, Any, Sequence
from langgraph.graph import END, START, add_messages
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

class StateAgent(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    
class RouterQuery(BaseModel): # decision making
    """Route a user query to the most relevant datasource."""
    webservice = " "
    datasource:Literal[webservice] = Field(
        ...,
        description="Given a user question choose to route it to webservice.",
    )
    
    

system_prompt = SystemMessage(
    content=(
        "You are an AI Career Coach specializing in helping students and professionals improve their resumes. "
        "Your job is to review resumes and provide **specific, actionable, and constructive feedback**. "
        "You should:\n"
        "1. Identify strengths (skills, achievements, clarity).\n"
        "2. Point out weaknesses (vague wording, lack of quantifiable results, formatting issues).\n"
        "3. Suggest improvements in a structured way (bullet points, sections).\n"
        "4. Check for ATS (Applicant Tracking System) friendliness — ensure keywords, proper sectioning, and formatting.\n"
        "5. Tailor suggestions to the career path (e.g., Data Analyst, Software Engineer, Business Analyst).\n"
        "6. Be concise but thorough — avoid generic advice like 'make it better'.\n"
        "7. Always provide examples of better phrasing or formatting when possible.\n\n"
        "Tone: Encouraging, professional, and supportive. Avoid sounding robotic.\n"
        "Goal: Help the user land more interviews by making their resume stronger."
    )
)

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

    
    
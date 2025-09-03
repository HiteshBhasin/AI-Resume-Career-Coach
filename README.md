# AI-Resume-Career-Coach
An immediate market in the student network.

resume-coach-app/
│
├── frontend/                     # React app (student uploads resume here)
│   ├── src/
│   │   ├── components/           # UI components
│   │   │   ├── UploadResume.js   # Upload form
│   │   │   ├── ResumePreview.js  # Preview uploaded resume
│   │   │   ├── Feedback.js       # AI-generated feedback UI
│   │   │   └── CareerTips.js
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── Dashboard.js
│   │   │   └── Profile.js
│   │   ├── api/                  # API calls to backend
│   │   │   └── resumeApi.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── backend/                      # FastAPI/Flask backend with LangGraph
│   ├── app/
│   │   ├── main.py               # FastAPI entry point
│   │   ├── routers/
│   │   │   ├── resume.py         # Endpoints for resume upload & processing
│   │   │   └── feedback.py       # Endpoints for AI feedback
│   │   ├── services/
│   │   │   ├── resume_ingestion.py # Splitting, embedding, storing resumes
│   │   │   ├── feedback_agent.py   # LangGraph pipeline for resume review
│   │   │   └── career_tips_agent.py# LangGraph pipeline for career guidance
│   │   ├── vectorstore/          # Storage for embeddings
│   │   │   ├── chroma/           # Example: Chroma DB persistence
│   │   └── utils/
│   │       ├── parsers.py        # Resume parsing (PDF/DOCX to text)
│   │       └── text_cleaner.py   # Clean & normalize text
│   └── requirements.txt
│
├── langgraph_flows/              # LangGraph-specific flows
│   ├── resume_analysis_graph.py  # Graph for analyzing resume
│   ├── career_coach_graph.py     # Graph for career Q&A
│   └── feedback_graph.py         # Graph for AI improvement suggestions
│
├── docs/                         # Documentation & planning
│   ├── 10-week-plan.md
│   └── architecture.md
│
└── README.md


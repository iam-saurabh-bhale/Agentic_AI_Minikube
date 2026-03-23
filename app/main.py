from fastapi import FastAPI
from pydantic import BaseModel

from Agents.Agent_Bot import run_agent_bot
from Agents.Memory_Agent import run_memory_agent
from Agents.ReAct import run_react_agent
from Agents.Drafter import run_drafter_agent
from Agents.RAG_Agent import run_rag_agent

app = FastAPI()

class Request(BaseModel):
    message: str
    session_id: str = "default"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent")
def agent(req: Request):
    return {"response": run_agent_bot(req.message)}


@app.post("/memory")
def memory(req: Request):
    return {"response": run_memory_agent(req.session_id, req.message)}


@app.post("/react")
def react(req: Request):
    return {"response": run_react_agent(req.message)}


@app.post("/drafter")
def drafter(req: Request):
    return {"response": run_drafter_agent(req.session_id, req.message)}


@app.post("/rag")
def rag(req: Request):
    return {"response": run_rag_agent(req.message)}
#This file receives the request, calls a function from another file, and returns the final JSON response to the user.
from fastapi import FastAPI,Path,Query
from typing import Annotated
from app.github_client import fetch_user,fetch_repos,fetch_events
from app.schemas import GitHubUser,GitHubRepo,GitHubEvent
from typing import Literal

app = FastAPI(title="GitPulse")

@app.get("/")
def health():
    return {"status" : "ok","message":"GitPulse is running"}  

@app.get("/user/{username}",response_model = GitHubUser )
async def get_user( username : Annotated[str,Path(description="Enter a github username")] ):
    return await fetch_user(username)

@app.get("/user/{username}/repos",response_model = list[GitHubRepo])
async def get_repos(username : str,
                    repo_type : str = "owner",
                    per_page : int = Query(default=100,gt=0,le=100),
                    sort : Literal["created","updated","full_name","pushed"] = "updated"):
    return await fetch_repos(username,repo_type,per_page,sort)

@app.get("/user/{username}/events",response_model=list[GitHubEvent])
async def get_events(username : str,per_page : int = Query(default=100,gt=0,le=100)):
    return await fetch_events(username,per_page)
from typing import Optional,Annotated,Literal
from pydantic import BaseModel,Field

class GitHubUser(BaseModel):
    #Only these fields are required from raw user data
    login : str
    name : Optional[str] = None
    bio: Optional[str] = None
    id : int
    location : Optional[str] = None
    public_repos: int
    followers : int
    avatar_url: str
    created_at : str
    updated_at : str
    email : Optional[str] = None
    twitter_username: Optional[str] = None

class License(BaseModel):
    key : str
    name : str

class GitHubRepo(BaseModel):
    name : str
    description : Optional[str] = None
    fork : Annotated[bool,Field(description="Is the repo forked?")]
    forks : Annotated[int,Field(description="Total forks for repo")]  
    topics : list[str] = []
    updated_at : str
    license : Optional[License] = None
    stargazers_count : Annotated[int,Field(description="Total stars for repo")] 
    language : Optional[str] = None  #this just gives the primary lang,but for lang breakdown u need to fetch the langs from languages_url,
                                     #that would again make 51 api calls if the user has 50 repos,which is a huge mess!!!!!
    '''
    #later,we can implement db as mentioned in issue #15 
    languages_url : str
    '''
class Repo(BaseModel):
    name : str

class GitHubEvent(BaseModel):
    type : Annotated[Literal["PushEvent","PullRequestEvent","IssuesEvent","IssueCommentEvent"],Field(description = "Event is any one of these")]
    created_at : str
    repo : Repo  #we only need repo["name"]


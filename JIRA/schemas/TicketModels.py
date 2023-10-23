from pydantic import BaseModel, Field, constr, EmailStr, SecretStr
from typing import Optional, List, Literal
from datetime import datetime
from enum import Enum


class TicketCreate(BaseModel):
    title: str = "Example Title"
    description: str = "This is an example description for the Jira ticket."
    priority: str = "High"
    due_date: str = "2023-12-31"
    project_id: Optional[str] = "Project123"


class TicketUpdate(BaseModel):
    title: Optional[str] = "Example Title"
    description: Optional[str] = "This is an example description for the Jira ticket."
    priority: Optional[str] = "High"
    due_date: Optional[str] = "2023-12-31"
    project_id: Optional[str] = "Project123"
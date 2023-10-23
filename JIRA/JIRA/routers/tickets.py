from typing import Annotated
from fastapi import Depends, APIRouter, Query, Header
from pydantic import UUID4
from JIRA.core import definitions as variables
from JIRA.schemas import TicketModels
from JIRA.app.ticket.ticketAPI import ticket_management_object

jira_routes = APIRouter(prefix=variables.BASE_URL + "ticket")
# ---------------------- Jira Management ------------------


@jira_routes.post("/create")
async def create_jira_ticket(request_info: TicketModels.TicketCreate):
    source = ticket_management_object.create_ticket(request_info)
    return source

@jira_routes.put("/update")
async def update_jira_ticket_by_ticket_id(ticket_id: str, ticket_update: TicketModels.TicketUpdate):
    source = ticket_management_object.update_ticket(ticket_id, ticket_update)
    return source

@jira_routes.get("/search-ticket")
async def get_ticket_details_by_ticket_id(ticket_id: str):
    source = ticket_management_object.search_ticket(ticket_id)
    return source
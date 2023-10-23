from fastapi import APIRouter,HTTPException
# from JIRA.database.jiraTicket import create_ticket, get_ticket, update_ticket, delete_ticket
# from JIRA.database import jiraTicket

class TicketManagementClass(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Ticket Management Class"

    def create_ticket(self,request_info):
        try:
            # Define the ticket data
            ticket_data = {
                "TicketID": "unique-ticket-id",  # Generate a unique ticket ID
                "Title": request_info.title,
                "Description": request_info.description,
                "Priority": request_info.priority,
                "DueDate": request_info.due_date,
                "ProjectID": request_info.project_id
            }

            # Insert the ticket data into DynamoDB
            # response = jiraTicket.create_ticket(ticket_data)

            # return {"message": "Jira ticket created successfully", "ticket_id": ticket_data["TicketID"]}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating Jira ticket: {str(e)}")


    def update_ticket(self,ticket_id,ticket_update):
        pass

    def search_ticket(self,ticket_id):
        pass

ticket_management_object = TicketManagementClass()
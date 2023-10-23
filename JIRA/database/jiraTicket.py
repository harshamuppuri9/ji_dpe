from JIRA.database.database import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("JiraTickets")


def create_ticket(ticket: dict):
    try:
        table.put_item(Item=ticket)
        return ticket
    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)


def get_ticket(TicketID: str):
    try:
        response = table.query(KeyConditionExpression=Key("LoaderId").eq(TicketID))
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)


def get_songs():
    try:
        response = table.scan(
            Limit=200,
            AttributesToGet=[
                "SongId",
                "SongTittle",
                "Artist",
                "SongGenre",
                "SongProductionDate",
                "LoaderId",
                "LoaderName",
            ],
        )
        return response["Items"]

    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)


def delete_ticket(ticket: dict):
    try:
        response = table.delete_item(Key={"TicketID": ticket["TicketID"]})
        return response

    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)


def update_ticket(ticket: dict):
    try:
        response = table.update_item(
            Key={"TicketID": ticket["TicketID"]},
            UpdateExpression="SET #T = :Title, #D = :Description, #P = :Priority, #Dd = :DueDate",
            ExpressionAttributeValues={
                ":Title": ticket["Title"],
                ":Description": ticket["Description"],
                ":Priority": ticket["Priority"],
                ":DueDate": ticket["DueDate"],
            },
            ExpressionAttributeNames={
                "#T": "Title",
                "#D": "Description",
                "#P": "Priority",
                "#Dd": "DueDate",
            },
        )

        return response

    except ClientError as e:
        return JSONResponse(content=e.response["error"], status_code=500)

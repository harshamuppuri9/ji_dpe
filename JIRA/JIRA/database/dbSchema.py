table_user = {
    "TableName": "Users",
    "AttributeDefinitions": [
        {"AttributeName": "UserID", "AttributeType": "S"},  # S for string attribute
        {"AttributeName": "Username", "AttributeType": "S"},
        {"AttributeName": "Email", "AttributeType": "S"},
    ],
}

table_project = {
    "TableName": "Projects",
    "AttributeDefinitions": [
        {"AttributeName": "ProjectID", "AttributeType": "S"},  # S for string attribute
        {"AttributeName": "ProjectName", "AttributeType": "S"},
        {"AttributeName": "Description", "AttributeType": "S"},
        {"AttributeName": "ProjectStatus", "AttributeType": "S"},
    ],
}

table_projectMembers = {
    "TableName": "ProjectsMembers",
    "AttributeDefinitions": [
        {"AttributeName": "ProjectID", "AttributeType": "S"},  # S for string attribute
        {"AttributeName": "UserID", "AttributeType": "S"},
        {"AttributeName": "UserType", "AttributeType": "S"},
    ],
}

table_jiraTickets = {
    "TableName": "JiraTickets",
    "AttributeDefinitions": [
        {"AttributeName": "TicketID", "AttributeType": "S"},  # S for string attribute
        {"AttributeName": "ProjectID", "AttributeType": "S"},  # S for string attribute
        {"AttributeName": "Creator", "AttributeType": "S"},
        {"AttributeName": "Assignee", "AttributeType": "S"},
        {"AttributeName": "Status", "AttributeType": "S"},
    ],
}

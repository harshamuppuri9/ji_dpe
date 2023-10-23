import requests
import json

# Define your Jira instance URL and API endpoint
base_url = f"https://your-instance-name.atlassian.net"
issue_endpoint = "/rest/api/2/issue/"

# Set your Jira credentials
username = "kartik21gupta04@gmail.com"
api_token = "token"

# Construct the issue data
issue_data = {
    "fields": {
        "project": {
            "key": "PROJECT_KEY"
        },
        "summary": "Summary of the issue",
        "description": "Detailed description of the issue",
        "issuetype": {
            "name": "Bug"  # Or any other issue type
        }
    }
}

# Convert the data to JSON format
issue_data_json = json.dumps(issue_data)

# Set headers for the request
headers = {
    "Content-Type": "application/json"
}

# Create the Jira issue
url = f"{base_url}{issue_endpoint}"
response = requests.post(url, auth=(username, api_token), data=issue_data_json, headers=headers)

if response.status_code == 201:
    print("Jira issue created successfully")
    print("Issue Key:", response.json()["key"])
else:
    print("Failed to create Jira issue")
    print("Status Code:", response.status_code)
    print("Response Content:", response.text)

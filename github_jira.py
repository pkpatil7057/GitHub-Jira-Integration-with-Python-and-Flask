import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask 

# Creating a flask app instance
app = Flask(__name__)

@app.route("/createJira", methods=['POST'])
def createJira():
    url = "https://pkpatil7057.atlassian.net/rest/api/3/issue"

    api_token = ""

    auth = HTTPBasicAuth("your@gmail.com", api_token)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10003"
        },
        "project": {
        "key": "SCRUM"
        },
        "summary": "First jira ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





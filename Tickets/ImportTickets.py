import requests

host = "cloudsufi.zendesk.com"
url = "https://" + host + "/api/v2/imports/tickets"
username = "poojan.trivedi@cloudsufi.com/token"
password = "67Wp6CGTSZ5HQP679IDg3NwPihOV1qupDGLBusPD"


def getUniqueTicketBody(ticketprefix, ticketsuffix):
    body = {
        "ticket": {
            "assignee_id": 5449860535965,
            "comments": [
                {
                    "author_id": 5469233188509,
                    "created_at": "2009-06-25T10:15:18Z",
                    "value": "This is a comment"
                },
                {
                    "author_id": 5449860535965,
                    "public": "false",
                    "value": "This is a private comment"
                }
            ],
            "description": "A description",
            "requester_id": 5469233188509,
            "subject": ticketprefix.format(ticketsuffix),
            "tags": [
                "foo",
                "bar"
            ]
        }
    }

    return body


for x in range(20, 1000):
    response = requests.post(url, auth=(username, password), json=getUniqueTicketBody("TestTicketAAA{}", x))
    print(response.text)

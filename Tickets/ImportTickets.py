import requests
import threading

host = "cloudsufi.zendesk.com"
url = "https://" + host + "/api/v2/imports/tickets?async=true"
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


def createtickets(ticketprefix, startingindex, endingindex):
    for x in range(startingindex, endingindex):
        requests.post(url, auth=(username, password), json=getUniqueTicketBody("TestTicket" + ticketprefix + "{}", x))


t1 = threading.Thread(target=createtickets, args=("AAC", 1, 25000))
t2 = threading.Thread(target=createtickets, args=("AAD", 1, 25000))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")

import requests
import threading

host = "cloudsufi.zendesk.com"
url = "https://" + host + "/api/v2/imports/tickets?async=true"
agentOneUsername = "poojan.trivedi@cloudsufi.com/token"
agentTwoUsername = "vikas.rathee@cloudsufi.com/token"
token = "67Wp6CGTSZ5HQP679IDg3NwPihOV1qupDGLBusPD"


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


def createtickets(agentUsername, ticketprefix, startingindex, endingindex):
    for x in range(startingindex, endingindex):
        requests.post(url, auth=(agentUsername, token), json=getUniqueTicketBody("TestTicket" + ticketprefix + "{}", x))


t1 = threading.Thread(target=createtickets, args=(agentOneUsername, "A3AABB", 1, 100000))
t2 = threading.Thread(target=createtickets, args=(agentOneUsername, "A3ABBB", 1, 100000))
t3 = threading.Thread(target=createtickets, args=(agentOneUsername, "A3ACBB", 1, 100000))
t4 = threading.Thread(target=createtickets, args=(agentOneUsername, "A3ADBB", 1, 100000))
t5 = threading.Thread(target=createtickets, args=(agentOneUsername, "A3AEBB", 1, 100000))
t6 = threading.Thread(target=createtickets, args=(agentOneUsername, "A3AFBB", 1, 100000))
t7 = threading.Thread(target=createtickets, args=(agentTwoUsername, "A33AABB", 1, 100000))
t8 = threading.Thread(target=createtickets, args=(agentTwoUsername, "A33ABBB", 1, 100000))
t9 = threading.Thread(target=createtickets, args=(agentTwoUsername, "A33ACBB", 1, 100000))
t10 = threading.Thread(target=createtickets, args=(agentTwoUsername, "A33ADBB", 1, 100000))
t11 = threading.Thread(target=createtickets, args=(agentTwoUsername, "A33AEBB", 1, 100000))
t12 = threading.Thread(target=createtickets, args=(agentTwoUsername, "A33AFBB", 1, 100000))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()

print("Done!")

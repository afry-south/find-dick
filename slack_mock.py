
class SlackBot:
    def __init__(self, token):
        pass

    def getUserId(self, email):
        print("Getting user ID for " + email)
        return email

    def sendMessage(self, userId, message):
        print("Sending message to: " + userId)
        print(message)
        return ""
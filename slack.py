import requests
import json

class SlackBot:
    headers = {}
    def __init__(self, token):
        self.headers = {'Authorization' : 'Bearer ' + token}

    def getUserId(self, email):
        url = 'https://slack.com/api/users.lookupByEmail'
        params = {'email' : email}
        res = requests.get(url, params=params, headers=self.headers)
        print(res.text)
        id = json.loads(res.text)['user']['id']
        return id

    def sendMessage(self, userId, message):
        url = 'https://slack.com/api/chat.postMessage'
        data = {"text" : message, "channel" : userId}
        res = requests.post(url, headers=this.headers, data=data)
        return res
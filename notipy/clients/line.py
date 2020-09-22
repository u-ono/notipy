import requests


class LineClient:

    url = 'https://notify-api.line.me/api/notify'

    def __init__(self, token):

        self.headers = {'Authorization': 'Bearer ' + token}

    def send(self, msg):

        params = {'message': msg}
        return requests.post(self.url, params=params, headers=self.headers)

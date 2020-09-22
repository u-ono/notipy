import requests


class SlackClient:

    def __init__(self, token, channel, check_redundancy_func=None):
        self.token = token
        self.channel = channel

        if check_redundancy_func:
            self.is_redundant = check_redundancy_func
        else:
            self.is_redundant = lambda msg: 'Traceback' in msg

    def send(self, msg):
        if self.is_redundant(msg):

            files = {'file': msg}

            param = {
                'token': self.token,
                'channels': self.channel,
            }
            requests.post(url="https://slack.com/api/files.upload", params=param, files=files)

        else:
            params = {
                'token': self.token,
                'channel': self.channel,
                'text': msg
            }
            requests.post(url="https://slack.com/api/chat.postMessage", params=params)

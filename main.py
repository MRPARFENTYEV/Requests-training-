import json
import pprint
import requests

Token = cdсв



class YandexDisc:
    def __init__(self, token):
        self.token = token
        print(token)

    def get_headers(self):
        return {
            'Content-Type': 'application/Json',
            'Authorization': 'OAuth{}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        print(headers)
        response = requests.get(files_url, headers=headers)
        return response.json()

    if __name__ == '__main__':
        ya = YandexDisc(Token)
        pprint(ya.get_files_list())

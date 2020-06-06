from requests import request, Response
from json.decoder import JSONDecoder

method_base = "https://api.vk.com/method/"

decoder = JSONDecoder()
with open('access.json', 'rt') as f:
    json = ''
    line = f.readline()
    while line:
        json += line
        line = f.readline()

access = decoder.decode(json)
access_token = f'access_token={access["access_token"]}&v={access["APIv"]}'


def get_user(idf: str) -> dict:
    return request('GET', method_base + f'users.get?user_ids={idf}&{access_token}').json()


def get_friends(idf: int) -> dict:
    return request('GET', method_base + f'friends.get?user_id={idf}&{access_token}&fields=nickname').json()

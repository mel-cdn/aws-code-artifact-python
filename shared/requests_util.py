import json
from typing import Union

import requests


class RequestsUtil:

    def __init__(self, bearer_token: str):
        self.__session = requests.Session()
        self.__session.headers.update(
            {
                "content-type": "application/json",
                "Authorization": f"Bearer {bearer_token}"
            }
        )

    def get(self, url: str, params: dict) -> Union[dict, list]:
        response = self.__session.get(url=url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, url: str, body: dict) -> Union[dict, list]:
        response = self.__session.post(url=url, data=json.dumps(body))
        response.raise_for_status()
        return response.json()

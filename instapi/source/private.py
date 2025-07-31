import requests
import json, re
from .. import config
from .user import InstagramUser


class InstagramRequest(InstagramUser):
    def __init__(self, cookie: str, useragent: str = None) -> None:
        self.session = requests.session()
        self.session.cookies['cookie'] = cookie

        self.base_source = self.session.get(config.BASE_URL).text
        self.headers_api = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/ivan.fmsyh','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Linux"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' if useragent is not None else useragent,'x-asbd-id': '359341','x-csrftoken': re.search(r'"csrf_token":"(.*?)"', self.base_source).group(1),'x-ig-app-id': '936619743392459','x-ig-www-claim': re.search(r'"claim":"(.*?)"', self.base_source).group(1),'x-instagram-ajax': '1025144473','x-requested-with': 'XMLHttpRequest','x-web-session-id': '',}
        self.headers_graphql = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"','sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"23108RN04Y"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36' if useragent is not None else useragent,'x-asbd-id': '359341','x-csrftoken': re.search(r'"csrf_token":"(.*?)"', self.base_source).group(1)}

    @InstagramUser.login
    def graphql(self, data: dict, headers: dict = None) -> json:
        request = self.session.post(config.BASE_URL +'graphql/query', data=data, headers=headers if headers else self.headers_graphql)
        return request.json()

    @InstagramUser.login
    def api(self, endpoint: str, params: dict = None, headers: dict = None) -> json:
        request = self.session.get(config.BASE_URL + endpoint, params=params if params else {}, headers=headers if headers else self.headers_api)
        return request.json()


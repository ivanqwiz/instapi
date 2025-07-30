from .source.private import InstagramRequest

class Client(InstagramRequest):
    def __init__(self, cookie: str):
        super().__init__(cookie=cookie)
        self.is_login = True if self.extract_user_information() else False


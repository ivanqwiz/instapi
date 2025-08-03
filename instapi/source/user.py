import re, json
from .nested import auto_dataclass, dataclass_from_dict
from ..exceptions import CookieError, UserNotFound, GraphqlError
from .. import config, utils
from requests.exceptions import JSONDecodeError


class InstagramUser:
    def login(func):
        def wrapper(self, *args, **kwargs):
            if not self.is_login:
                raise CookieError('Invalid cookie. Please use another cookie!!!')           
            return func(self, *args, **kwargs)
        return wrapper

    @login 
    def user_information(self, username: str) -> dataclass_from_dict:
        try:
            user = self.api(endpoint='/api/v1/users/web_profile_info/', params={'username': username})['data']['user']
            user_information_dict = {"username": user.get("username"),"id": user.get("id"),"full_name": user.get("full_name"),"biography": user.get("biography"),"followers": user.get("edge_followed_by", {}).get("count"),"following": user.get("edge_follow", {}).get("count"),"is_private": user.get("is_private"),"is_verified": user.get("is_verified"),"profile_pic_url": user.get("profile_pic_url_hd"),"mutual_followers": [edge["node"]["username"] for edge in user.get("edge_mutual_followed_by", {}).get("edges", [])]}
            return dataclass_from_dict(auto_dataclass('UserInformation', user_information_dict), user_information_dict)
        except JSONDecodeError:
            raise UserNotFound('User not found. Use another username!!!')

    def extract_user_information(self) -> bool:
        try:
            setattr(self, 'username', re.search(r'"username":"(.*?)"', self.base_source).group(1))
            setattr(self, 'id', re.search(r'"id":"(.*?)"', self.base_source).group(1))
            setattr(self, 'name', re.search(r'"full_name":"(.*?)"', self.base_source).group(1))
            return True
        except AttributeError:
            return False

    @login
    def unfollow(self, username: str) -> dataclass_from_dict:
        target = self.user_information(username=username)
        variables = json.dumps({"target_user_id":target.id,"container_module":"profile","nav_chain":"PolarisProfilePostsTabRoot:profilePage:1:via_cold_start"})

        payload = utils.payload(source=self.base_source)
        payload.update({'fb_api_req_friendly_name': 'usePolarisUnfollowMutation','variables': variables, 'server_timestamps': 'true','doc_id': '9846833695423773'})

        response = self.graphql(data=payload)
        if 'xdt_destroy_friendship' in str(response):
            data = {'full_name': target.full_name, 'id': target.id, 'username': target.username}
            return dataclass_from_dict(auto_dataclass('UnfollowUser', data), data)
        else:
            raise GraphqlError('Graphql api error. Please check your cookies!!!')

    @login 
    def follow(self, username: str) -> dataclass_from_dict:
        target = self.user_information(username=username)
        variables = json.dumps({"target_user_id":target.id,"container_module":"profile","nav_chain":"PolarisProfilePostsTabRoot:profilePage:1:via_cold_start"})

        payload = utils.payload(source=self.base_source)
        payload.update({'fb_api_req_friendly_name': 'usePolarisFollowMutation','variables': variables,'server_timestamps': 'true','doc_id': '9740159112729312'})

        response = self.graphql(data=payload)
        if 'xdt_create_friendship' in str(response):
            data = {'full_name': target.full_name, 'id': target.id, 'username': target.username}
            return dataclass_from_dict(auto_dataclass('FollowUser', data), data)
        else:
            raise GraphqlError('Graphql api error. Please check your cookies!!!')

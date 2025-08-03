import re, json
from .user import InstagramUser 
from .nested import dataclass_from_dict, auto_dataclass
from ..exceptions import GraphqlError, PostNotFound
from .. import config, utils 

class InstagramPost:
    @InstagramUser.login 
    def like(self, media_id: str = None, url: str = None) -> dataclass_from_dict:
        media_id = media_id if media_id else self.post_information(url=url).media_id
        variables = json.dumps({"media_id":media_id,"container_module":"single_post"})

        payload = utils.payload(source=self.base_source)
        payload.update({'fb_api_req_friendly_name': 'usePolarisLikeMediaLikeMutation','variables': variables,'server_timestamps': 'true','doc_id': '23951234354462179'})

        response = self.graphql(data=payload)
        if 'xdt_mark_media_like' in str(response):
            data = {'publisher_id': re.search(rf"{media_id}_(.*?)'", str(response)).group(1), 'media_id': media_id}
            return dataclass_from_dict(auto_dataclass('LikePost', data), data)
        else:
            raise PostNotFound('Post not found. Check your links or media_id.')

    @InstagramUser.login 
    def post_information(self, url: str) -> dataclass_from_dict:
        source = self.session.get(f'https://www.instagram.com/p/{url}/' if 'instagram.com' not in url else url).text 
        try:
            url = re.search(r'property="og:url" content="(.*?)"', source).group(1)
            data = {'media_id': re.search(r'instagram://media\?id=(.*?)"', source).group(1),'like_count': int(re.search(r'(\d+)\s+likes', source).group(1)),'comment_count': int(re.search(r'(\d+)\s+comments', source).group(1)),'url': url,'username': re.search(r'com/(.*?)/p/', url).group(1)}
            return dataclass_from_dict(auto_dataclass('PostInformation', data), data)
        except Exception as e:
            raise PostNotFound('Post not found. Check your links.')



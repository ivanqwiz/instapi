## Example of use
Sign in using cookies.

Use [extension](https://chromewebstore.google.com/detail/get-cookies/hdablekeodiopcnddiamhahahkiiloph) to retrieve cookies.
```python
>>> from instapi import Client

>>> COOKIE = 'datr=jsjs......' # your cookie string
>>> ig = Client(cookie=COOKIE)
```
Retrieving account data.
```python
>>> ig.name # full name your account 
'Ivan Firmansyah'
>>> ig.username # username your account
'ivan.fmsyh'
>>> ig.id # your account id
'65122884339'
```

## User information 
```python
>>> target_username = 'ivan.fmsyh'
>>> data = ig.user_information(username=target_username) # retrieving user data
User(username='ivan.fmsyh', id='65122884339', full_name='Ivan Firmansyah', biography='', followers=63, following=22, is_private=False, is_verified=False, profile_pic_url='https://scontent.cdninstagram.com/v/t51.2885-19/498568319_17899751043194534_5028882398275736674_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2QFHqIJ1bCv5PNMH7HkPVLk95rpWlZORHrnchMk7X3VILW_B6zuyXq77NLSbMm6ZKZ4&_nc_ohc=_miLC92vB60Q7kNvwEsAKM-&_nc_gid=B-1CjcpfjtvbcufVHStzYQ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfQDufb4N_65CJ7vW3Mhu80O14K2KW3RkvpukpMSh0Irnw&oe=688F5D25&_nc_sid=8b3546', mutual_followers=['winaa3957'])
```
Example of retrieving one of the user's information.
```python
>> data.username # get username
'ivan.fmsyh'
```

## Unfollow user
```python
>>> data = ig.unfollow(username=target_username)
UnfollowUser(full_name='Ivan Firmansyah', id='65122884339', username='ivan.fmsyh')
```

## Follow user
```python
>>> data = ig.follow(username=target_username)
FollowUser(full_name='Ivan Firmansyah', id='65122884339', username='ivan.fmsyh')
```

## Post information
```python
>>> data = ig.post_information(url='https://insta...')
PostInformation(media_id='3690780662392912400', like_count=13, comment_count=0, url='https://www.instagram.com/jurnalpantura.id/p/DM4SXU1z3oQ/', username='jurnalpantura.id')
```

## Like post
```python
>>> data = ig.like(url='https://istagra...') # or use media_id='3690780....'
LikePost(publisher_id='6012782922', media_id='3690780662392912400')
```

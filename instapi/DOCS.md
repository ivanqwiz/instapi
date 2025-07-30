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

>> data.username # get username
'ivan.fmsyh'
```

## Unfollow user
```python
>>> target_username = 'ivan.fmsyh'
>>> data = ig.unfollow(username=target_username)
UnfollowUser(full_name='Ivan Firmansyah', id='65774138533', username='ivan.fmsyh', is_private=False, profile_pic_url='https://scontent.cdninstagram.com/v/t51.2885-19/498568319_17899751043194534_5028882398275736674_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2QH6WeO6DnmKLmP8KKR9kGo4WooATt9siEP8-rrMZgLXE81gZWC6nd-z5kg3HsGwJR8&_nc_ohc=_miLC92vB60Q7kNvwEsAKM-&_nc_gid=EiU-DW-5P61FTWwFjE8h8g&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfSBy1P0rKkgebC3X9KXuhAqVUlJerDZ6OT7Ll3nZ-tqaQ&oe=688FCDA5&_nc_sid=8b3546')

>>> data.full_name # get target name
'Ivan Firmansyah'
```

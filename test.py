from instapi import Client 

x = Client(cookie='')
print(x.is_login)
x.unfollow(username='abcs')

from instapi import Client 

x = Client('datr=N3KAaKEGbz2ZWbEj1K5zzmmB; ig_did=91E41F0C-2704-46A3-ACE3-018E3C0CA9DB; mid=aIByNwABAAFDBD5ss27FyYbViOr9; ps_l=1; ps_n=1; dpr=2.1988937854766846; ig_nrcb=1; csrftoken=P9ZQ53Vo5xBaKdZoCJuP5sI3fqJMPxTZ; ds_user_id=65122884339; sessionid=65122884339%3AaSUq986UUGZedR%3A1%3AAYdDNZF3FYMGmDc0JrWGGBUHmiJirPOLvMUQ-w2SFw; wd=891x1718; rur="EAG\05465122884339\0541785497695:01fececd5cbc5e441b579daa11fcc808b9f2e800c632df28486234ba2aef19101a1cadbe"')
print(x.username)
print(x.like(url='https://www.instagram.com/jurnalpantura.id/p/DM4SXU1z3oQ/'))

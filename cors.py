import re
import pandas as ps
import requests
import random
import time
from bs4 import BeautifulSoup
import json
def ask_url():
    headers = {
        'Origin':'https://attacker.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        'Cookie': 'bid=6mHemZBr91A; __gads=ID=f6d1e29943a2289e-2235597b46cf0014:T=1637928036:RT=1637928036:S=ALNI_MbUV2rRDkg5u38czBTVDBFS0PLajA; ll="108305"; _vwo_uuid_v2=D05DF24F53B472D086C01A79B01735762|e5e120c8d217d8191d1303c2a5b5aa04; gr_user_id=6441c017-d74b-422f-af14-93a11a57112d; __yadk_uid=tajeNgKg6NT6nhEQczKfmecGcZqdVBXY; douban-fav-remind=1; __utmv=30149280.23512; _ga=GA1.2.1042859692.1637928038; viewed="2995812_1458367_6816154_1416697_1455695_1986653_1395176_3040149_1427374_4913064"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1652841585%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVlfhYZ2MEHRBSLvH1rcPwd4AYRrL-DQrWxaEeqtUjfETnWetwL98pNUbJ__vgCwN%26wd%3D%26eqid%3Da1df55aa0002864e0000000662845c64%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1042859692.1637928038.1649577909.1652841585.36; __utmb=30149280.0.10.1652841585; __utmc=30149280; __utmz=30149280.1652841585.36.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1442664133.1641956556.1648885892.1652841585.22; __utmb=223695111.0.10.1652841585; __utmc=223695111; __utmz=223695111.1652841585.22.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="235123238:u9rdv3vTMd0"; ck=nl8E; _pk_id.100001.4cf6=023cbddd8ff1a247.1641956556.21.1652843267.1648885892.; push_noty_num=0; push_doumail_num=0'
    }
    with open('./cors.txt','r') as fr:
        for line in fr:
            geturl = line
            geturl=geturl.replace('\n','')
            try:
                response=requests.get(geturl,headers=headers,timeout=5)
                par=response.headers.get('Access-Control-Allow-Origin')
                if par == "https://attacker.com":
                    print(geturl)
                else:
                    continue
            except Exception as e:
                pass
                continue
ask_url()


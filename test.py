import urllib.request as urllib2
import urllib.parse
from bs4 import BeautifulSoup
import requests

'''url = 'http://www.tycqxs.com/82_82814/30502244.html'
ua_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

request = urllib2.Request(url ,headers=ua_headers)
response = urllib2.urlopen(request)
html = response.read()
print(response.getcode())
print(response.geturl())
print(response.info())
soup = BeautifulSoup(html)
print(html)'''

urlBuff = 'https://buff.163.com/market/goods?goods_id=42964&from=market'


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    # cookie
cookie_str = r'Device-Id=18M5mJB9aNR6sROw3Uf3; nts_mail_user=shenej0026@163.com:-1:1; mail_psc_fingerprint=bba38f509eb19ccb5633b2dd363968b7; _ntes_nnid=38e8eaa3a8c419cb6275ed8ad00f2b28,1609842450913; _ntes_nuid=38e8eaa3a8c419cb6275ed8ad00f2b28; Locale-Supported=zh-Hans; game=csgo; _ga=GA1.2.731519374.1610172052; _gid=GA1.2.995557773.1610172052; NTES_YD_SESS=.D5vEGjtx_U8ydt.E8xHwTB9vy4YAcTUbPfTRyB_RD7gmVb8mPEkn1tzPlJLwbiUsFJObY9.kLG0KeKTOCtEO09UCDhZwVmJsBBujHjThtCkp4.jYNxuxQHMoLa9_lZ15Ng..qBBoU_E1.T4PuJetMTYinzlKb7T0E7kyFipJFv_ZPBjlhHW0ht7b7kN1sLOKlDK0d8E2BOrTHaLLyQr3GOHtt0V5mg74p49mVSi4PEKt; S_INFO=1610173594|0|3&80##|17640052174; P_INFO=17640052174|1610173594|1|netease_buff|00&99|hub&1610172518&netease_buff#hub&420100#10#0#0|&0|null|17640052174; remember_me=U1092088919|3tiLfJqOhfBYdZJI5RvlYBnFE5IXpCA4; session=1-UxyAZflStZf4-hpza9jAix0JLzBR-cpVf_iSCLn0eHXJ2044291855; csrf_token=IjdiY2ViMTNkZDFhNjQ0NTJhMmRmMmQzYWQ4ZmMyOGIxOGNkMmRkMjEi.Etrj5g.AnWVL-hYtGTKpLt4EoKZLQuwNas'

buffcookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    buffcookies[key] = value
html = requests.get(url=urlBuff,headers=headers,cookies=buffcookies)
soup = BeautifulSoup(html.text,'lxml')
data = soup.select('#sell_order_210107T1365708640 > td:nth-child(5) > div:nth-child(1) > strong')
print(data)
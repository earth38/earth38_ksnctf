import base64

f = open("a")
data = f.read() 
#デコードする回数を指定
n = int(input("input times >>"))
for i in range(n):
    data = base64.b64decode(data)

#byte型からstr型に変換してから出力
print(data.decode('utf-8'))


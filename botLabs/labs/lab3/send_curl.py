import requests
import json
from botsetting.config import SECRET_KEY

url = "https://api.openai.com/v1/chat/completions"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + SECRET_KEY
}


def payload(q):
    return json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": q
            }
        ],
    })


def send_request(q):
    response = requests.request("POST", url, headers=headers, data=payload(q))
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        res = response.json()['choices'][0]['message']['content']
        print(res)
        return res
    else:
        return "Ошибка выполнения запроса. Повторите попытку"


if __name__ == '__main__':
    send_request("")

import json


def parse_json(text):
    try:
        json_object = json.loads(text)
        return json_object.keys(), json_object.values()
    except:
        return "Ошибка в исходных данных", "Попробуйте еще раз"


if __name__ == '__main__':
    print(parse_json('{"test":"1","test2":"2","test3":"3","test4":"4","test5":"5"}'))

import requests
import time


def get_ans(question, model=False):
    # 获取当前时间的时间戳
    timestamp = int(time.time() * 1000)

    # # 将时间戳转换为 datetime 对象
    # dt_obj = datetime.datetime.fromtimestamp(timestamp / 1000)
    #
    # # 将 datetime 对象转换为 timestamp 对象
    # timestamp_obj = datetime.datetime.timestamp(dt_obj)

    url = 'https://api.aichatos.cloud/api/generateStream'

    headers = {
        "authority": "api.aichatos.cloud",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://chat1.aichatos.com",
        "pragma": "no-cache",
        "referer": "https://chat1.aichatos.com/",
        "sec-ch-ua": "^\\^Chromium^^;v=^\\^112^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    proxy_address = 'http://127.0.0.1:10809'

    data = {"prompt": question,
            "userId": "#/chat/{}".format(timestamp),
            "network": True,
            "system": "",
            "withoutContext": False,
            "stream": False}

    response = requests.post(url=url, headers=headers, json=data)
    response.encoding = 'utf-8'
    return response.text
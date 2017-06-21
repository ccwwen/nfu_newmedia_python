from pprint import pprint
import requests
import json
import time

def output(data):
    # 这里有三个注意的点：
    # 1. mode="a"
    # 2. "{}\n" 一条结果一行
    # 3. ensure_ascii=False
    # 我没怎么在python3下处理编码的问题，我试了一下你的代码不能正确输出中文
    # 得加上ensure_ascii=False
    with open ("bencao_detail2", mode="a", encoding='utf8') as file:
        file.write("{}\n".format(json.dumps(data, ensure_ascii=False)))


q = list(range(1, 1771))  #构造一个简单的队列，起始是1

while len(q):  # 队列还有就执行
    n = q.pop(0)  # 取出队列的第一个
    print("Fetching No.{}".format(n))  # 这里输出到哪一步了，可以帮助你从断点处重来
    url_api = "http://api.jisuapi.com/bencao/detail?appkey=bdc8ee0bb0227112&detailid={n}&isdetailed={n}".format(n=n)
    try:
        r = requests.get (url_api,timeout=3.05)
    except Exception as e:
        print("Exception: {}".format(e))
        q.append(n)  # 出错放回到队列尾部
    else:
        data = r.json()
        pprint(data)
        output(data)
    time.sleep(2)  # 还是设置一个等待吧，太快的访问容易被屏蔽。可以自己改

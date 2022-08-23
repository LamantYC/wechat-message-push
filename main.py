import time
import random
import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
nowDate = time.strftime("%H:%M:%S", time.localtime(time.time()))


def getweek():
    weekEng = time.strftime("%A", time.localtime(time.time()))
    week_list = {
        "Monday": "星期一",
        "Tuesday": "星期二",
        "Wednesday ": "星期三",
        "Thursday": "星期四",
        "Friday": "星期五",
        "Saturday": "星期六",
        "Sunday": "星期日"
    }
    week = week_list[weekEng]
    return week


# 获取城市天气状况
def getcitytq():
    params = {
        "key": "SiPRODFFnHm7MghEe",
        "location": "jinan",  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
    }
    url = 'https://api.seniverse.com/v3/weather/now.json'
    resp = requests.get(url, params)
    if resp.status_code:
        data = resp.json()["results"]
        return data
    else:
        print('请求失败')


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 获取空气质量
def getkqzl():
    params = {
        "key": "SiPRODFFnHm7MghEe",
        "location": "jinan",  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
        "days": "1"
    };
    url = 'https://api.seniverse.com/v3/life/suggestion.json'
    resp = requests.get(url, params)
    if resp.status_code:
        data = resp.json()["results"]
        return data
    else:
        print('请求失败')


# 获取每日心灵鸡汤语录(没找到合适的API)
soupUrl = 'https://apis.juhe.cn/fapig/soup/query?key='

# 处理获取到的数据
address = getcitytq()[0]["location"]['name']  # 地点
temperature = getcitytq()[0]['now']["temperature"]  # 温度
weather = getcitytq()[0]['now']["text"]  # 天气情况
suggestion = getkqzl()[0]['suggestion'][0]['air_pollution']['brief']

# 推送消息
client = WeChatClient('wx7d6cc98124f0149f', '2d8eececc62002cf941b50be3d8da911')
wm = WeChatMessage(client)
user_id = 'ohW5U6kZ_q00GnkJ5fYZWalpYEZo'

if "06:00:00" < nowDate < "11:00:00":
    template_id = 'pdfxbQfzkqNMNRHWguCdQX3i_8deyMu4HLHyLsfgUcE'
    data = {
        "date": {"value": currentTime, "color": get_random_color()},
        "week": {"value": getweek(), "color": get_random_color()},
        "city": {"value": address, "color": get_random_color()},
        "weather": {"value": weather, "color": get_random_color()},
        "kqtype": {"value": suggestion, "color": get_random_color()},
        "tem": {"value": temperature + '℃', "color": get_random_color()},
    }
if "11:00:00" < nowDate < "14:00:00":
    template_id = 'fvxNrCL9nq3MMxi_DstlnKkBtsnpsYAm62wxURWe2NY'
    data = {
        "nowDate": {"value": nowDate, "color": get_random_color()},
        "week": {"value": getweek(), "color": get_random_color()},
        "city": {"value": address, "color": get_random_color()},
        "weather": {"value": weather, "color": get_random_color()},
        "kqtype": {"value": suggestion, "color": get_random_color()},
        "tem": {"value": temperature + '℃', "color": get_random_color()},
    }
if "14:00:00" < nowDate < "18:00:00":
    template_id = 'U7ZvonOp9jRdpc9J2X7FwdjLEqs-ZogbzUnFYU9K2jY'
    data = {
        "nowDate": {"value": nowDate, "color": get_random_color()},
        "week": {"value": getweek(), "color": get_random_color()},
        "city": {"value": address, "color": get_random_color()},
        "weather": {"value": weather, "color": get_random_color()},
        "kqtype": {"value": suggestion, "color": get_random_color()},
        "tem": {"value": temperature + '℃', "color": get_random_color()},
    }
if "18:00:00" < nowDate < "24:00:00":
    template_id = 'M5U2l1QiNWCxN8q5LLj6LaIOPDi3T3NDHn2VLDmh2k0'
    data = {
        "nowDate": {"value": nowDate, "color": get_random_color()},
        "week": {"value": getweek(), "color": get_random_color()},
        "city": {"value": address, "color": get_random_color()},
        "weather": {"value": weather, "color": get_random_color()},
        "kqtype": {"value": suggestion, "color": get_random_color()},
        "tem": {"value": temperature + '℃', "color": get_random_color()},
    }

resp = wm.send_template(user_id, template_id, data)

print(resp)
print("当前时间：", currentTime, '-', nowDate, '-', getweek())
print('位置天气：', address, '-', temperature + '℃', '-', weather, '-', suggestion)

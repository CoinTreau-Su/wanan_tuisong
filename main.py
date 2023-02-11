import random
from time import time, localtime
import cityinfo
from requests import get, post
from datetime import datetime, date
import sys
import os
import http.client, urllib
import json
from zhdate import ZhDate
global false, null, true
false = null = true = ''
def get_color():
    # 获取随机颜色
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0xC7EDCC, 0xCCE8CF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)


def get_access_token():
    # appId
    app_id = config["app_id"]
    # appSecret
    app_secret = config["app_secret"]
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
                .format(app_id, app_secret))
    try:
        access_token = get(post_url).json()['access_token']
    except KeyError:
        print("获取access_token失败，请检查app_id和app_secret是否正确")
        os.system("pause")
        sys.exit(1)
    # print(access_token)
    return access_token



def get_weather(province, city):
    # 城市id
    try:
        city_id = cityinfo.cityInfo[province][city]["AREAID"]
    except KeyError:
        print("推送消息失败，请检查省份或城市是否正确")
        os.system("pause")
        sys.exit(1)
    # city_id = 101280101
    # 毫秒级时间戳
    t = (int(round(time() * 1000)))
    headers = {
        "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://d1.weather.com.cn/dingzhi/{}.html?_={}".format(city_id, t)
    response = get(url, headers=headers)
    response.encoding = "utf-8"
    response_data = response.text.split(";")[0].split("=")[-1]
    response_json = eval(response_data)
    # print(response_json)
    weatherinfo = response_json["weatherinfo"]
    # 天气
    weather = weatherinfo["weather"]
    # 最高气温
    temp = weatherinfo["temp"]
    # 最低气温
    tempn = weatherinfo["tempn"]
    return weather, temp, tempn




#彩虹屁
def caihongpi():
    if (Whether_caihongpi!=False):
        try:
            conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
            params = urllib.parse.urlencode({'key':tianxing_API})
            headers = {'Content-type':'application/x-www-form-urlencoded'}
            conn.request('POST','/caihongpi/index',params,headers)
            res = conn.getresponse()
            data = res.read()
            data = json.loads(data)
            data = data["result"][0]["content"]
            if("XXX" in data):
                data.replace("XXX","宝贝老婆")
            return data
        except:
            return ("彩虹屁API调取错误，请检查API是否正确申请或是否填写正确")

#健康小提示API
def health():
    if (Whether_health!=False):
        try:
            conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
            params = urllib.parse.urlencode({'key':tianxing_API})
            headers = {'Content-type':'application/x-www-form-urlencoded'}
            conn.request('POST','/healthtip/index',params,headers)
            res = conn.getresponse()
            data = res.read()
            data = json.loads(data)
            data = data["result"][0]["content"]
            return data
        except:
             return ("健康小提示API调取错误，请检查API是否正确申请或是否填写正确")

#生活小窍门API
def lifetip():
    try:
        conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':tianxing_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/qiaomen/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        if data["code"] == 200:
            data = data["result"]["content"]
        else:
            data = "有问题！找老公！找老公！~"
        return data
    except:
         return ("生活小窍门API调取错误，请检查API是否正确申请或是否填写正确")

#土味情话API
def tuweiqinghua():
    try:
        conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':tianxing_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/saylove/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        if data["code"] == 200:
            data = data["result"]["content"]
        else:
            data = "咦~~出了点问题！啵唧老婆一口吧"
        return data
    except:
         return ("土味情话API调取错误，请检查API是否正确申请或是否填写正确")

#晚安心语API
def wananxinyu():
    try:
        conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':tianxing_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/wanan/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        if data["code"] == 200:
            data = data["result"]["content"]
        else:
            data = "老婆晚安啦~good night~"
        return data
    except:
         return ("晚安心语API调取错误，请检查API是否正确申请或是否填写正确")

#古代情诗API
def gudaiqingshi():
    try:
        conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':tianxing_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/qingshi/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        if data["code"] == 200:
            content = data["result"]["content"]
            source  = data["result"]["source"]
            data = content
        else:
            data = "你是一树一树的花开，是燕，在梁间的呢喃，是爱，是暖，是希望，你是人间的四月天。~"
        return data
    except:
         return ("古代情诗API调取错误，请检查API是否正确申请或是否填写正确")

#下雨概率和建议
def tip():
    if (Whether_tip!=False):
        try:
            conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
            params = urllib.parse.urlencode({'key':tianxing_API,'city':city,'type':1})
            headers = {'Content-type':'application/x-www-form-urlencoded'}
            conn.request('POST','/tianqi/index',params,headers)
            res = conn.getresponse()
            data = res.read()
            data = json.loads(data)
            tips = data["result"]["tips"]
            alarmlist = data["result"]["alarmlist"]
            if len(alarmlist) == 0 :
                alarm = '嘻嘻~气象台没有报警呢~'
            else :
                alarm = data["result"]["alarmlist"]["content"]

            return alarm,tips
        except:
            return ("天气预报API调取错误，请检查API是否正确申请或是否填写正确"),""

#推送信息
def send_message(to_user, access_token,  xinyu , qingshi ):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() % 7]

    data = {
        "touser": to_user,
        "template_id": config["template_id"],
        "url": "http://weixin.qq.com/download",
        "topcolor": "#FF0000",
        "data": {
            "date": {
                "value": "{} {}".format(today, week),
                #"color": get_color()
            },
            # "city": {
            #     "value": city_name,
            #     #"color": get_color()
            # },
            # "weather": {
            #     "value": weather,
            #     #"color": get_color()
            # },
            # "min_temperature": {
            #     "value": min_temperature,
            #     #"color": get_color()
            # },
            # "max_temperature": {
            #     "value": max_temperature,
            #     #"color": get_color()
            # },
            # "alarm": {
            #     "value": alarm,
            #     # "color": get_color()
            # },
            "lifetips": {
                "value": lifetips,
                # "color": get_color()
            },
            "qinghua": {
                "value": qinghua,
                # "color": get_color()
            },
            "xinyu": {
                "value": xinyu,
                # "color": get_color()
            },
            "qingshi": {
                "value": qingshi,
                # "color": get_color()
            },


            "qinghua": {
                "value": qinghua,
                # "color": get_color()
            },
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = post(url, headers=headers, json=data).json()
    if response["errcode"] == 40037:
        print("推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("推送消息成功")
    else:
        print(response)


if __name__ == "__main__":
    try:
        with open("./config.json", encoding="utf-8") as f:
            config = eval(f.read())
    except FileNotFoundError:
        print("推送消息失败，请检查config.txt文件是否与程序位于同一路径")
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("推送消息失败，请检查配置文件格式是否正确")
        os.system("pause")
        sys.exit(1)

    # 获取accessToken
    accessToken = get_access_token()
    # 接收的用户
    users = config["user"]
    # 传入省份和市获取天气信息
    province, city = config["province"], config["city"]
    weather, max_temperature, min_temperature = get_weather(province, city)
    #获取天行API
    tianxing_API=config["tianxing_API"]
    #是否开启天气预报API
    Whether_tip=config["Whether_tip"]
    # #是否启用词霸每日一句
    # Whether_Eng=config["Whether_Eng"]
    # #是否启用星座API
    # Whether_lucky=config["Whether_lucky"]
    # #是否启用励志古言API
    # Whether_lizhi=config["Whether_lizhi"]
    # #是否启用彩虹屁API
    # Whether_caihongpi=config["Whether_caihongpi"]
    # #是否启用健康小提示API
    # Whether_health=config["Whether_health"]
    # #获取星座
    # astro = config["astro"]
    # # 获取词霸每日金句
    # note_ch, note_en = get_ciba()
    # #彩虹屁
    # pipi = caihongpi()
    # #健康小提示
    # health_tip = health()
    # #下雨概率和建议
    alarm,tips = tip()
    # #生活小建议
    lifetips = lifetip()
    # #土味情话
    qinghua = tuweiqinghua()
    # #晚安心语
    xinyu   = wananxinyu()
    # #睡前故事
    qingshi = gudaiqingshi()
    # #励志名言
    # lizhi = lizhi()
    # #星座运势
    # lucky_ = lucky()

    # 公众号推送消息
    for user in users:
        send_message(user, accessToken, xinyu , qingshi)
    import time
    time_duration = 3.5
    time.sleep(time_duration)

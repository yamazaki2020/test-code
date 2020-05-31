# -*- coding: utf-8 -*-

import sys
import pandas as pd
import urllib.request
# アメダス実況(神奈川県)
url = "https://tenki.jp/amedas/3/17/"
# LINE_Notify
LINE_TOKEN="XXXXXXXXXXXXXXXXX" #access token
LINE_NOTIFY_URL="https://notify-api.line.me/api/notify"


def get_temperature_info():
    try:    
        dfs = pd.read_html(url, encoding="UTF-8")
        df = dfs[0]
        # DataFrame 0行目:"横浜"
        r = 0
        city = str(df.iloc[r, 0])   #0列目:"地点名"
        temperture = float(df.iloc[r, 1])   #1列目:"気温(℃)"
        precipitation = float(df.iloc[r, 2])    #2列目:"降水量(mm/h)"
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)

    msg1 = "\n地点： {}\n気温： {}℃\n降水： {}mm/h".format(city, temperture,  precipitation)

    return(msg1)


def send_weather_info(msg2):
    method = "POST"
    headers = {"Authorization": "Bearer %s" % LINE_TOKEN}
    payload = {"message": msg2}
    try:
        payload = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url=LINE_NOTIFY_URL, data=payload, method=method, headers=headers)
        urllib.request.urlopen(req)
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)


def main():
    msg = get_temperature_info()
    send_weather_info(msg)    


if __name__ == "__main__":
    main()

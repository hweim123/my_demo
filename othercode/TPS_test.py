import threading
import requests
import hashlib
from time import *
from datetime import datetime
import json


THREAD_NUM = 10
LOOP_NUM = 10
sum_time = 0.00
success_count = 0

# c = login_response.cookies
# content =


def order():
    # global c
    global sum_time
    global success_count
    t1 = time()
    url = "http://mcp.yinmei.me:8081/mcp/v2/sys/PrintHtmlUrl"
    form_data = {"app_id": "a123456", "access_token": "t123456", "merchant_code": "ym",
                 "device_ids": "16480045WP", "copies": "1", "cus_orderid": t1, "bill_type": 3,
                 "bill_content": "http://dev-open.yinmei.me/content/Upload/yingmei.html", "time_out": 60}
    make_response = requests.post(url, form_data)
    res = make_response.text
    # print(res)
    code = json.loads(res)["return_code"]
    assert code == 0
    print("请求成功")
    # time = datetime.now() + timedelta(hours=1)
    t2 = time()
    res_time = t2 - t1
    result = open("F:\\res.txt", "a")
    result.write("成功订单响应时间："+str(res_time)+"\n")
    result.close()
    sum_time = sum_time + res_time
    success_count = success_count + 1
    # print(success_count)


def looptest():
    global LOOP_NUM
    for i in range(0, LOOP_NUM):
        order()


def main():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=looptest, name="T"+str(i))
        # print("-----", t, "------")
        t.setDaemon(True)
        Threads.append(t)
    for n in Threads:
        n.start()
    for n in Threads:
        n.join()


if __name__ == "__main__":
    t3 = time()
    main()
    t4 = time()
    total_time = t4 - t3
    result = open("F:\\res.txt", "a")
    result.write("并发订单总数："+str(THREAD_NUM*LOOP_NUM)+"\n")
    result.write("成功订单数："+str(success_count)+"\n")
    result.write("总响应时间："+str(sum_time)+"\n")
    result.write("total_time: "+str(total_time)+"\n")
    result.write("成功订单平均响应时间："+str(sum_time/success_count)+"\n")
    result.write("TPS："+str(success_count/(sum_time/success_count))+"\n")
    result.write("TPS_1: "+str(success_count/(total_time/success_count))+"\n")
    result.close()


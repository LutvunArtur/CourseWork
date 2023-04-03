from argparse import ArgumentParser
import json
from random import randint
json_file = "work.json"
json_data_file = "data.json"


def upd_json_file(some_data, file_name=json_data_file):
    with open(file_name, "w", encoding="utf-8") as my_data:
        result = json.dump(some_data, my_data)


with open(json_file, encoding="utf-8") as my_file:
    res = json.load(my_file)

with open(json_data_file, encoding="utf-8") as data_file:
    data_res = json.load(data_file)


trader = ArgumentParser()
trader.add_argument("action", type=str, nargs="?")
trader.add_argument("num", type=str, nargs="?")
trader = vars(trader.parse_args())


class Trade:
    def __init__(self, data, result):
        self.data_res = data
        self.res = result
        self.data_course = self.data_res["course"]
        self.data_ua = self.data_res["UA"]
        self.data_usd = self.data_res["USD"]
        self.data_delta = self.data_res["delta"]
        self.fst_course = self.res["course"]
        self.fst_ua = self.res["UA"]
        self.fst_usd = self.res["USD"]
        self.fst_delta = self.res["delta"]

    def rate(self):
        return round(self.fst_course, 2) if data_res == 0 else round(self.data_course, 2)

    def available(self):
        return f"{round(self.fst_ua, 2)} UA, {round(self.fst_usd, 2)} USD" if data_res == 0 else \
            f"{round(self.data_ua, 2)} UA, {round(self.data_usd,  2)} USD"

    def buy_all(self):
        if data_res == 0:
            res_dict = {}
            self.fst_usd += self.fst_ua / self.fst_course
            self.fst_ua = 0
            res_dict["UA"] = round(self.fst_ua, 2)
            res_dict["USD"] = round(self.fst_usd, 2)
            res_dict["course"] = round(self.fst_course, 2)
            res_dict["delta"] = round(self.fst_delta, 2)
        else:
            res_dict = {}
            self.data_usd += self.data_ua / self.data_course
            self.data_ua = 0
            res_dict["UA"] = round(self.data_ua, 2)
            res_dict["USD"] = round(self.data_usd, 2)
            res_dict["course"] = round(self.data_course, 2)
            res_dict["delta"] = round(self.data_delta, 2)
        return res_dict

    def sell_all(self):
        if data_res == 0:
            res_dict = {}
            self.fst_ua += self.fst_usd * self.fst_course
            self.fst_usd = 0
            res_dict["UA"] = round(self.fst_ua, 2)
            res_dict["USD"] = round(self.fst_usd, 2)
            res_dict["course"] = round(self.fst_course, 2)
            res_dict["delta"] = round(self.fst_delta, 2)
        else:
            res_dict = {}
            self.data_ua += self.data_usd * self.data_course
            self.data_usd = 0
            res_dict["UA"] = round(self.data_ua, 2)
            res_dict["USD"] = round(self.data_usd, 2)
            res_dict["course"] = round(self.data_course, 2)
            res_dict["delta"] = round(self.data_delta, 2)
        return res_dict

    @staticmethod
    def restart():
        upd_json_file(res)

    def buy_some(self, some_num):
        if self.data_res == 0:
            res_dict = {}
            if self.fst_ua < some_num:
                raise Exception("You dont have enough money")
            upd_json_file(res)
            self.fst_usd += some_num
            res_ua = self.fst_ua - (some_num * self.data_course)
            res_dict["UA"] = round(res_ua, 2)
            res_dict["USD"] = round(self.fst_usd, 2)
            res_dict["course"] = round(self.fst_course, 2)
            res_dict["delta"] = round(self.fst_delta, 2)
        else:
            res_dict = {}
            if self.data_ua < some_num:
                raise Exception("You dont have enough money")
            self.data_usd += some_num
            res_ua = self.data_ua - (some_num * self.data_course)
            res_dict["UA"] = round(res_ua, 2)
            res_dict["USD"] = round(self.data_usd, 2)
            res_dict["course"] = round(self.data_course, 2)
            res_dict["delta"] = round(self.data_delta, 2)
        return res_dict

    def sell_some(self, some_num):
        if self.data_res == 0:
            res_dict = {}
            if self.fst_usd < some_num:
                raise Exception("You dont have enough usd")
            self.fst_ua += some_num * self.fst_course
            self.fst_usd = self.fst_usd - some_num
            res_dict["UA"] = round(self.fst_ua, 2)
            res_dict["USD"] = round(self.fst_usd, 2)
            res_dict["course"] = round(self.fst_course, 2)
            res_dict["delta"] = round(self.fst_delta, 2)
        else:
            res_dict = {}
            if self.data_usd < some_num:
                raise Exception("You dont have enough usd")
            self.data_ua += some_num * self.data_course
            self.data_usd = self.data_usd - some_num
            res_dict["UA"] = round(self.data_ua, 2)
            res_dict["USD"] = round(self.data_usd, 2)
            res_dict["course"] = round(self.data_course, 2)
            res_dict["delta"] = round(self.data_delta, 2)
        return res_dict

    def next(self):
        rand_num = randint(1, 10)
        if self.data_res == 0:
            res_dict = {}
            res_course = self.fst_course + self.fst_delta if rand_num < 5\
                else self.fst_course - self.fst_delta
            res_dict["UA"] = round(self.fst_ua, 2)
            res_dict["USD"] = round(self.fst_usd, 2)
            res_dict["course"] = round(res_course, 2)
            res_dict["delta"] = round(self.fst_delta, 2)
        else:
            res_dict = {}
            res_course = self.data_course + self.data_delta if rand_num < 5 \
                else self.data_course - self.data_delta
            res_dict["UA"] = round(self.data_ua, 2)
            res_dict["USD"] = round(self.data_usd, 2)
            res_dict["course"] = round(res_course, 2)
            res_dict["delta"] = round(self.data_delta, 2)
        return res_dict


trader_ex = Trade(data_res, res)
if trader["action"] == "RATE":
    print(round(trader_ex.rate(), 2))
elif trader["action"] == "AVAILABLE":
    print(trader_ex.available())
elif trader["action"] == "BUY":
    if trader["num"] == "ALL":
        upd_json_file(trader_ex.buy_all())
        print("done")
    elif trader["num"] == int:
        upd_json_file(trader_ex.buy_some(trader["num"]))
        print("done!")
elif trader["action"] == "SELL":
    if trader["num"] == "ALL":
        upd_json_file(trader_ex.sell_all())
        print("done!")
    elif trader["num"] == int:
        upd_json_file(trader_ex.sell_some(trader["num"]))
        print("done!")
elif trader["action"] == "RESTART":
    trader_ex.restart()
    print("done!")
elif trader["action"] == "NEXT":
    upd_json_file(trader_ex.next())
    print("done!")
else:
    print("Wrong request, try again")

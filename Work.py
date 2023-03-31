from argparse import ArgumentParser
import json
json_file = "work.json"
json_data_file = "Data.json"


def upd_json_file(some_data, file_name=json_data_file):
    with open(file_name,"w", encoding="utf-8") as my_data:
        ress = json.dump(my_data, some_data)


with open(json_file, encoding="utf-8") as my_file:
    res = json.load(my_file)
fst_course = res["курс"]
fst_ua = res["на гривневому рахунку"]
fst_usd = res["на доларовому рахунку"]
fst_delta = res["дельта"]
with open(json_data_file, encoding="utf-8") as data_file:
    data_res = json.load(data_file)
data_course = data_res["курс"]
data_ua = data_res["на гривневому рахунку"]
data_usd = data_res["на доларовому рахунку"]
data_delta = data_res["дельта"]

# nextt,  buy_some, sell_some


class Trade:
    def __init__(self, rate, available, buy_all, sell_all, restart):
        self.rate = rate
        self.available = available
        self.buy_all = buy_all
        self.sell_all = sell_all
        self.restart = restart
        # self.next = nextt
        # self.buy_some = buy_some
        # self.sell_some = sell_some
        self.date_ua = data_ua
        self.date_usd = data_usd
        self.date_course = data_course
        self.date_delta = data_delta
        self.frst_ua = fst_ua
        self.frst_usd = fst_usd
        self.frst_course = fst_course
        self.frst_delta = fst_delta
        self.date_res = data_res

    def rate(self):
        return fst_course if data_res == 0 else self.date_course

    def available(self):
        return f"{fst_ua} UA, {fst_usd} USD" if data_res == 0 else f"{self.date_ua} UA, {self.date_usd} USD"

    def buy_all(self):
        if data_res == 0:
            self.date_ua += fst_ua * fst_course
            result = self.date_usd
        else:
            self.date_ua += self.date_ua * self.date_course
            result = self.date_usd
        upd_json_file(result)
        return result

    def sell_all(self):
        if data_res == 0:
            self.date_ua += fst_usd / fst_course
            result = self.date_ua
        else:
            self.date_ua = self.date_usd / self.date_course
            result = self.date_ua
            upd_json_file(result)
        return result

    def restart(self):
        self.date_res = res


trader = ArgumentParser()
trader.add_argument("RATE", type=str, nargs="?")
trader.add_argument("AVAILABLE", type=str, nargs="?")
trader.add_argument("BUY ALL", type=str, nargs="?")
trader.add_argument("SELL ALL", type=str, nargs="?")
trader.add_argument("NEXT", type=str, nargs="?")
trader.add_argument("RESTART", type=str, nargs="?")
# trader.add_argument(, nargs="?")
# trader.add_argument(, nargs="?")
trader = vars(trader.parse_args())
trader_ex = Trade(rate=trader["RATE"], available=trader["RATE"], buy_all=trader["BUY ALL"], sell_all=trader["SELL ALL"],
                  restart=trader["RESTART"])
trader["RATE"] = trader_ex.rate()
trader["AVAILABLE"] = trader_ex.available()
trader["BUY ALL"] = trader_ex.buy_all()
trader["SELL ALL"] = trader_ex.sell_all()
# trader["NEXT"] = Trade.nextt


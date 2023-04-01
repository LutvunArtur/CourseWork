from argparse import ArgumentParser
import json
json_file = "work.json"
json_data_file = "Data.json"


def upd_json_file(some_data, file_name=json_data_file):
    with open(file_name, "w", encoding="utf-8") as my_data:
        ress = json.dump(my_data, some_data)


with open(json_file, encoding="utf-8") as my_file:
    res = json.load(my_file)

with open(json_data_file, encoding="utf-8") as data_file:
    data_res = json.load(data_file)

buy_some = input()
sell_some = input()
trader = ArgumentParser()
trader.add_argument("RATE", type=str, nargs="?")
trader.add_argument("AVAILABLE", type=str, nargs="?")
trader.add_argument("BUY", type=str, nargs="?")
trader.add_argument("SELL", type=str, nargs="?")
trader.add_argument("ALL", typr=str, nargs="?")
trader.add_argument("NEXT", type=str, nargs="?")
trader.add_argument("RESTART", type=str, nargs="?")
trader.add_argument(buy_some, type=int, nargs="?")
# trader.add_argument(, nargs="?")
trader = vars(trader.parse_args())


class Trade:
    def __init__(self, data, ress):
        self.buy_someth = buy_some
        self.sell_someth = sell_some
        self.data_res = data
        self.res = ress
        self.data_course = self.data_res["курс"]
        self.data_ua = self.data_res["на гривневому рахунку"]
        self.data_usd = self.data_res["на доларовому рахунку"]
        self.data_delta = self.data_res["дельта"]
        self.fst_course = self.res["курс"]
        self.fst_ua = self.res["на гривневому рахунку"]
        self.fst_usd = self.res["на доларовому рахунку"]
        self.fst_delta = self.res["дельта"]

    def rate(self):
        return self.fst_course if data_res == 0 else self.data_course

    def available(self):
        return f"{round(self.fst_ua, 2)} UA, {round(self.fst_usd, 2)} USD" if data_res == 0 else f"{round(self.data_ua, 2)} UA, {round(self.data_usd,  2)} USD"

    def buy_all(self):
        if data_res == 0:
            self.fst_usd += self.fst_ua * self.fst_course
            result = self.fst_usd
        else:
            self.data_ua += self.data_ua * self.data_course
            result = self.data_usd
        upd_json_file(result)
        return result

    def sell_all(self):
        if data_res == 0:
            self.fst_ua += self.fst_usd / self.fst_course
            result = self.data_ua
        else:
            self.data_ua = self.data_usd / self.data_course
            result = self.data_ua
        upd_json_file(result)
        return result

    def restart(self):
        self.data_res = res

    def buy_some(self):
        result = None
        if self.data_res == 0:
            self.fst_ua += self.buy_someth * self.fst_course
            if self.fst_ua < self.buy_someth:
                print("You dont have enough money")
                pass
            result = self.fst_ua
        else:
            self.data_ua += self.buy_someth * self.data_course
            if self.data_ua < self.buy_someth:
                print("You dont have enough money")
                pass
            result = self.data_ua
        upd_json_file(result)
        return result

    def sell_some(self):
        result = None
        if self.data_res == 0:
            self.fst_ua += self.sell_someth * self.fst_course
            if self.fst_usd < self.sell_someth:
                print("You dont have enough usd")
                pass
            result = self.fst_ua
        else:
            self.data_ua += self.sell_someth * self.data_course
            if self.data_usd < self.sell_someth:
                print("You dont have enough usd")
                pass
            result = self.data_ua
        upd_json_file(result)
        return result


trader_ex = Trade(data_res, res)
if trader["RATE"]:
    print(round(trader_ex.rate(), 2))
elif trader["AVAILABLE"]:
    print(trader_ex.available())
elif trader["BUY"]:
    if trader["ALL"]:
        trader_ex.buy_all()
        print(round(trader_ex.buy_all(), 2))
    elif trader[buy_some] == int(input()):
        trader_ex.buy_some()
        print(round(trader_ex.buy_some(), 2))
elif trader["SELL"]:
    if trader["ALL"]:
        trader_ex.sell_all()
        print(trader_ex.sell_all())
    elif trader[buy_some]:
        trader_ex.buy_some()
        print(trader_ex.buy_some())


from argparse import ArgumentParser
import json
json_file = "work.json"
json_data_file = "Data.json"


def upd_json_file(some_data, file_name=json_data_file):
    with open(file_name, "w", encoding="utf-8") as my_data:
        result = json.dump(my_data, some_data)
    return None


with open(json_file, encoding="utf-8") as my_file:
    res = json.load(my_file)

with open(json_data_file, encoding="utf-8") as data_file:
    data_res = json.load(data_file)


trader = ArgumentParser()
trader.add_argument("action", type=str, nargs="?")
trader.add_argument("num", type=int, nargs="?")
trader = vars(trader.parse_args())


class Trade:
    def __init__(self, data, result):
        self.data_res = data
        self.res = result
        self.data_course = self.data_res["курс"]
        self.data_ua = self.data_res["на гривневому рахунку"]
        self.data_usd = self.data_res["на доларовому рахунку"]
        self.data_delta = self.data_res["дельта"]
        self.fst_course = self.res["курс"]
        self.fst_ua = self.res["на гривневому рахунку"]
        self.fst_usd = self.res["на доларовому рахунку"]
        self.fst_delta = self.res["дельта"]

    def rate(self):
        upd_json_file(self.res) if data_res == 0 else None
        return self.fst_course if data_res == 0 else self.data_course

    def available(self):
        return f"{round(self.fst_ua, 2)} UA, {round(self.fst_usd, 2)} USD" if data_res == 0 else f"{round(self.data_ua, 2)} UA, {round(self.data_usd,  2)} USD"

    def buy_all(self):
        if data_res == 0:
            self.fst_usd += self.fst_ua * self.fst_course
            result = self.fst_usd
        else:
            self.data_usd += self.data_ua * self.data_course
            result = self.data_usd
        upd_json_file(result)
        return result

    def sell_all(self):
        if data_res == 0:
            upd_json_file(res) if data_res == 0 else None
            self.fst_ua += self.fst_usd / self.fst_course
            result = self.fst_usd
        else:
            self.data_ua = self.data_usd / self.data_course
            result = self.data_ua
        upd_json_file(result)
        return result

    @staticmethod
    def restart():
        upd_json_file(res)

    def buy_some(self, some_num):
        if self.data_res == 0:
            upd_json_file(res)
            self.fst_ua += some_num * self.fst_course
            if self.fst_usd < some_num:
                print("You dont have enough money")
                pass
            result = self.fst_ua
        else:
            self.data_ua += some_num * self.data_course
            if self.data_ua < some_num:
                print("You dont have enough money")
                pass
            result = self.data_ua
        upd_json_file(result)
        return result

    def sell_some(self, some_num):
        if self.data_res == 0:
            upd_json_file(res)
            self.fst_ua += some_num * self.fst_course
            self.fst_usd = self.fst_usd - some_num
            if self.fst_usd < some_num:
                print("You dont have enough usd")
            result = self.fst_ua, self.fst_usd
        else:
            self.data_ua += some_num * self.data_course
            self.data_usd = self.data_usd - some_num
            if self.data_usd < some_num:
                print("You dont have enough usd")
                pass
            result = self.data_ua,  self.data_usd
        upd_json_file(result)
        return result


trader_ex = Trade(data_res, res)
if trader["action"] == "RATE":
    print(round(trader_ex.rate(), 2))
elif trader["action"] == "AVAILABLE":
    print(trader_ex.available())
elif trader["action"] == "BUY":
    if trader["action"] == "ALL":
        trader_ex.buy_all()
        print("done")
    elif trader["action"] == trader["num"]:
        trader_ex.buy_some(trader["num"])
        print("DONE")
elif trader["action"] == "SELL":
    if trader["action"] == "ALL":
        trader_ex.sell_all()
        print("DONE")
    elif trader["action"] == trader["num"]:
        trader_ex.buy_some(trader["num"])
        print("DONE")
elif trader["action"] == "RESTART":
    trader_ex.restart()
    print("done!")
else:
    print("Wrong request, try again")

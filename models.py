import datetime
import requests


class Share:
    def __init__(self, code, company_name) -> None:
        self.code = code
        self.company_name = company_name
        self.prices = []
        self.dates = []
        self.actual_price = None
        self.isRising = None
        self.update()
    
    def update(self):
        self.prices = []
        self.dates = []
        today_str = str(datetime.date.today())
        two_week_ago_str = datetime.datetime.today() - datetime.timedelta(days=14)
        res = requests.get(f"http://iss.moex.com/iss/engines/stock/markets/shares/securities/{self.code}/candles.json?from={two_week_ago_str}&till={today_str}&interval=24")
        data = res.json()["candles"]["data"]
        for day in data:
            self.prices.append(day[1])
            self.dates.append(day[7].split(" ")[0])
        self.actual_price = self.prices[-1]
        self.isRising = self.prices[-1] > self.prices[-2]


shares = [
    Share("SBER", "СБЕР"),
    Share("VTBR", "ВТБ"),
    Share("YDEX", "Яндекс"),
    Share("VKCO", "Вконтакте"),
    Share("MGNT", "Магнит"),
    Share("OZON", "Озон"),
    Share("AFLT", "Аэрофлот"),
    Share("SMLT", "Самолёт")
]
import datetime
import requests


class Share:
    def __init__(self, code) -> None:
        self.code = code
        self.prices = []
        self.dates = []
        self.actual_price = None
    
    def update(self):
        today_str = str(datetime.date.today())
        two_week_ago_str = datetime.datetime.today() - datetime.timedelta(days=14)
        res = requests.get(f"http://iss.moex.com/iss/engines/stock/markets/shares/securities/{self.code}/candles.json?from={two_week_ago_str}&till={today_str}&interval=24")
        data = res.json()["candles"]["data"]
        for day in data:
            self.prices = day[1].split(" ")
            self.dates = day[7].split(" ")[0]
        self.actual_price = self.prices[-1]
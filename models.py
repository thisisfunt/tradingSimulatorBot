import datetime
import requests
import matplotlib.pyplot as plt
import schemas
from sqlalchemy.orm import Session

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
            # self.dates.append(day[7].split(" ")[0])
            date = day[7].split(" ")[0]
            year, month, day = date.split("-")
            date = day + "." + month
            self.dates.append(date)
        self.actual_price = self.prices[-1]
        self.isRising = self.prices[-1] > self.prices[-2]
        plt.clf()
        plt.plot(self.dates, self.prices, marker='o')
        plt.title(f"Изменение цены акций {self.company_name} за последние 2 недели")
        plt.xlabel("Дата")
        plt.ylabel("Цена (в руб.)")
        plt.grid(True)
        line_chart_file_name = f"line_charts/{self.code}.png"
        plt.savefig(line_chart_file_name)


def create_user_if_not_exist(tg_id: int):
    try:
        with Session(schemas.engine) as session:
            user = schemas.User(tg_id=tg_id, amount=50000)
            session.add(user)
            session.commit()
    except:
        pass


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

share_company_names = [share.company_name for share in shares]
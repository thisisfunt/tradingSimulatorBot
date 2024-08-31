# tradingSimulatorBot
Simple bot for simulate trading on stoke market


## Tech stack
1. aiogram 3.11.0
2. SQLAlchemy 2.0.32
3. mysql-connector-python 9.0.0
4. MySql
5. python-dotenv 1.0.1

## Run tutorial
1. Create python venv use `python -m venv venv`
2. Activate venv `.\venv\Scripts\activate.bat`
3. Install all requirements `pip install -r .\requirements.txt`
4. Edit .env file in "backend" (input your values)

## Arch. details
### classes:
**Share class**: a class whose objects store information about the company's shares
### modules:
**main.py**: run application <br>
**controllers.py**: take data from model.py, put view.py and send answers<br>
**views.py**: get data and return answer for user <br>
**models.py**: update data (prices) in cash, make transactions and return data from cash

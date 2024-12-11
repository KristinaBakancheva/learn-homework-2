"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta

def print_days():
    today = date.today()
    yesterday  = today-timedelta(1, 0, 0)
    before_30 = today-timedelta(30, 0, 0)
    print(f"вчера - {yesterday}, сегодня - {today}, 30 дней назад - {before_30}")


def str_2_datetime(date_string):
    return datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

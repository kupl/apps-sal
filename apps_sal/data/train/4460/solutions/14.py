from datetime import datetime


def whatday(n):
    return datetime(2019, 2, 2 + n).strftime("%A") if 1 <= n <= 7 else 'Wrong, please enter a number between 1 and 7'

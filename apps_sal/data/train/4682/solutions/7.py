from datetime import datetime, timedelta
from re import fullmatch


def date_correct(date):
    if isinstance(date, str):
        if not date:
            return ""
        if fullmatch("\d{2}\.\d{2}\.\d{4}", date):
            day, month, year = map(int, date.split("."))
            extra_year, month = divmod(month - 1, 12)
            return (datetime(year + extra_year, month + 1, 1) + timedelta(day - 1)).strftime("%d.%m.%Y")

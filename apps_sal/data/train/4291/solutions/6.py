
from math import ceil


def century(year):
    centuries, remaining = divmod(year, 100)
    return centuries + bool(remaining)


def century(year):
    return ceil(year / 100)


def century(year):
    return year // 100 + bool(year % 100)


def century(year):
    return year // 100 + (not not year % 100)


def century(year):
    return -(-year // 100)


def century(year):
    return (year + 99) // 100

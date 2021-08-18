from datetime import date


def unlucky_days(year):
    return sum(date(year, month, 13).isoweekday() == 5 for month in range(1, 13))


def __starting_point():
    assert unlucky_days(2015) == 3, "First - 2015"
    assert unlucky_days(1986) == 1, "Second - 1986"


__starting_point()

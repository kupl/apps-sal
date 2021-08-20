import calendar
from collections import deque


def whatday(num: int) -> str:
    """ Get weekday according to the input number (days rotated by 1). """
    days = deque(list(calendar.day_name))
    days.rotate(1)
    return dict(zip(list(range(1, 8)), days)).get(num, 'Wrong, please enter a number between 1 and 7')

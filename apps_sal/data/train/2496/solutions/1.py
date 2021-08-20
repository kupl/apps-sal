import calendar
import datetime


class Solution:

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return calendar.day_name[datetime.date(year, month, day).weekday()]

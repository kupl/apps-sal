import datetime
import calendar

class Solution:
    
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year, month, day).strftime('%A')

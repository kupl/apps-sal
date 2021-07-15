class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        diff_year = (year - 1971) % 7 + int((year - 1968)/4)
        print(('year:', (year - 1971), ':', (year - 1971)%7))
        print(('num leaps:', int((year - 1968)/4)))
        print(('diff_year:', diff_year))
        months = {1:0, 2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}
        print(('month add:', months[month]))
        if year == 2100:
            leap = -1
        elif month <=2 and (year - 1968)%4 == 0:
            leap = -1
        else:
            leap = 0
        weekdate = (diff_year + months[month] + day + leap -1)%7
        print(('day:', day))
        print(weekdate)
        weekdays = {5:'Wednesday', 6:'Thursday', 7:'Friday',0:'Friday', 
                    1:'Saturday', 2:'Sunday', 3: 'Monday', 4:'Tuesday'}
        return weekdays[weekdate]
        


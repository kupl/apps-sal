def days(date, month, year):
    current_year = 2437
    current_month = 3
    current_date = 24
    current_days = (24+28+31)
    days = 0
    y_days = 0
    
    print((date,month,year))
    
    def leap_year(year):
        condition = False
        if year > 1752:
            if year % 400 == 0:
                condition = True
            elif year % 100 == 0:
                condition = False
            elif year % 4 == 0:
                condition = True
        else:
            if year % 4 == 0:
                condition = True
        return condition
    
    month_30 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    month_30_leap = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    
    if year > 1752:
        if leap_year(year) == True: #if its a leap year
            for m in range(1,month):
                days += month_30_leap[m]
            days += date
            for y in range(year, current_year):
                if leap_year(y) == True:
                    y_days += 366
                else:
                    y_days += 365
            days = current_days - days + y_days
            print("this one - 1")
            return days
        else:
            for m in range(1,month):
                days += month_30[m]
            days += date
            for y in range(year, current_year):
                if leap_year(y) == True:
                    y_days += 366
                else:
                    y_days += 365
            days = current_days - days + y_days
            print("this one = 2")
            return days
    else:
        if year % 4 == 0:
        
            for m in range(1,month):
                days += month_30_leap[m]
                
            if year == 1752 and month > 9:
                days -= 11
                    
            if year == 1752 and month == 9:
            
                for d in range(1,date+1):
                    if 3 > d or d > 13:
                        print(d)
                        days += 1
            else:
                days += date
                
            for y in range(year, current_year):
                if leap_year(y) == True:
                    if y == 1752:
                        y_days += 366-11
                    else:
                        y_days += 366
                else:
                    y_days += 365
            days = current_days - days + y_days
            print("this one - 3")
            return days
            
        else:
            for m in range(1,month):
                days += month_30[m]

            days += date
                
            for y in range(year, current_year):
                if leap_year(y) == True:
                    if y == 1752:
                        y_days += 366-11
                    else:
                        y_days += 366
                else:
                    y_days += 365
            days = current_days - days + y_days
            print("this one - 4")
            return days
          


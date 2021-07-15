def am_I_afraid(day,num):
    return {'Monday'    : num == 12, 
            'Tuesday'   : num > 95, 
            'Wednesday' : num == 34, 
            'Thursday'  : not num, 
            'Friday'    : not (num % 2), 
            'Saturday'  : num == 56, 
            'Sunday'    : num == 666 or num == -666
           }[day]

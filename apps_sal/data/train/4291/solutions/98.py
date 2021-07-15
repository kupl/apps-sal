def century(year):
   
    
    if (year <= 0):
        return ("0 and negative is not allow for a year")
         
    
    
    elif (year <= 100):
        return (1)
    elif (year % 100 == 0):
        return (year // 100)
    else:
        return (year // 100 + 1)

def unlucky_days(year):
    import datetime
    
    # setting variables
    i, count = 1, 0
    
    # loop for each month
    while i <= 12:

        # checks if there is an unlucky day in the month
        if (datetime.datetime(year, i, 13).strftime('%w') ==  '5'): count += 1
        
        i += 1
        
    return count    

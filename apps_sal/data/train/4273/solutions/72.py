def shorten_to_date(long_date):
    newdate = long_date.replace(',','')
    lst = list(newdate.split(" "))
    listnew = lst[:4]
    
    return f"{listnew[0]} {listnew[1]} {listnew[2]}"

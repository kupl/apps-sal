import re    
def shorten_to_date(long_date):
    return re.sub(r",.+$",'',long_date)

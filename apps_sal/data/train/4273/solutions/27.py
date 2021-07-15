import re

def shorten_to_date(long_date):
    return re.match('[^,]+', long_date).group()

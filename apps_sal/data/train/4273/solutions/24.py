def shorten_to_date(long_date):
    splitString = long_date.split()
    return splitString[0] + " " + splitString[1] + " " + splitString[2].rstrip(',')

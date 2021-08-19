def shorten_to_date(long_date):
    long_date.split(', ')
    if '10pm' in long_date or '11pm' in long_date or '12pm' in long_date or ('10am' in long_date) or ('11am' in long_date) or ('12am' in long_date):
        return long_date[0:len(long_date) - 6]
    else:
        return long_date[0:len(long_date) - 5]

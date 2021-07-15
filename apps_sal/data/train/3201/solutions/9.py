from re import search
def validate_time(time):
    return bool(search('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', time))

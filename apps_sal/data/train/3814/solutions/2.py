from datetime import datetime


def get_military_time(time):
    return datetime.strptime(time, '%I:%M:%S%p').strftime('%H:%M:%S')

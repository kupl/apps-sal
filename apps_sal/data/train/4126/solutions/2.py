import time


def what_time_is_it(angle):
    return time.strftime('%I:%M', time.gmtime(angle * 2 * 60))

import time


def unlucky_days(y):
    return sum([time.strptime('%s-%d-13' % (y, x + 1), '%Y-%m-%d').tm_wday == 4 for x in range(12)])

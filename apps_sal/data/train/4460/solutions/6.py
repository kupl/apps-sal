WEEK = ' Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split(' ')


def whatday(n):
    return WEEK[n] if 0 < n < 8 else 'Wrong, please enter a number between 1 and 7'

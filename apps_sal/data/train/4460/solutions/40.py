from calendar import day_name


def whatday(n):
    return 'Wrong, please enter a number between 1 and 7' if n > 7 or n < 1 else day_name[n - 2]

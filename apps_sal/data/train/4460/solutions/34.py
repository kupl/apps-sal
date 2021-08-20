import calendar


def whatday(n):
    if not 1 <= n <= 7:
        return 'Wrong, please enter a number between 1 and 7'
    return calendar.day_name[(n - 2) % 7]

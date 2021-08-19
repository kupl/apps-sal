afraid = {'Monday': lambda x: x == 12, 'Tuesday': lambda x: x > 95, 'Wednesday': lambda x: x == 34, 'Thursday': lambda x: x == 0, 'Friday': lambda x: x % 2 == 0, 'Saturday': lambda x: x == 56, 'Sunday': lambda x: abs(x) == 666}


def am_I_afraid(day, num):
    return afraid[day](num)

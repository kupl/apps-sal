def clock_degree(s):
    (hour, minute) = map(int, s.split(':'))
    if not 0 <= hour < 24 or minute < 0:
        return 'Check your time !'
    hour %= 12
    minute %= 60
    return '{}:{}'.format(hour * 30 or 360, minute * 6 or 360)

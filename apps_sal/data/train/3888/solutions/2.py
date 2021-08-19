def clock_degree(s):
    (hours, minutes) = map(lambda str: int(str), s.split(':'))
    if hours < 0 or minutes < 0 or hours > 23 or (minutes > 59):
        return 'Check your time !'
    return str((hours % 12 or 12) * 30) + ':' + str((minutes or 60) * 6)

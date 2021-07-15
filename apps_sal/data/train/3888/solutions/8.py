def clock_degree(s) :
    hours, minutes = map(int, s.split(':'))
    return f"{hours % 12 * 30 or 360}:{minutes * 6 or 360}" if 0 <= hours < 24 and  0 <= minutes < 60 else "Check your time !"

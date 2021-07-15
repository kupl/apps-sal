def clock_degree(s) :
    hours, minutes = map(int, s.split(':'))
    return f"{hours % 12 * 30 if hours % 12 else 360}:{minutes * 6 if minutes % 60 else 360}" if 0 <= hours < 24 and  0 <= minutes < 60 else "Check your time !"

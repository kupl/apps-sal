def meeting_time(Ta, Tb, r):
    return f"{1/abs(1/(Ta or float('inf')) - 1/(Tb or float('inf')) or float('inf')):.2f}"

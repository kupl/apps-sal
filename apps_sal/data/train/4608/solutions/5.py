def finance(n):
    week = [sum(range(2*i, n+i+1)) for i in range(n+1)]
    return sum(week)

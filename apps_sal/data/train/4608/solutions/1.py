def finance(n):
    savings = 0
    for weeks in range(n+1):
        for days in range(weeks,n+1):
            savings += weeks + days
    return savings

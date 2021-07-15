next_day_of_week=lambda n,b:next(i%7+1for i in range(n,n+8)if 1<<i%7&b)

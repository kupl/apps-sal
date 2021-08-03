def next_day_of_week(n, b): return next(i % 7 + 1for i in range(n, n + 8)if 1 << i % 7 & b)

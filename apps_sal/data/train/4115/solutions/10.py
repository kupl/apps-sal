def find_outlier(num):
    odd = 0 if sum(n % 2 for n in num[:3]) > 1 else 1
    return next(n for n in num if n % 2 == odd)

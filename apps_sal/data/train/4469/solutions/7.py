def is_narcissistic(i):
    digits = str(i)
    n = len(digits)
    return sum(int(d)**n for d in digits) == i

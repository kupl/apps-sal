def is_narcissistic(i):
    s = str(i)
    return sum((int(x) ** len(s) for x in s)) == i

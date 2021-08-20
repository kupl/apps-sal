def is_narcissistic(i):
    return sum((int(d) ** len(str(i)) for d in str(i))) == i

def narcissistic(value):
    return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))


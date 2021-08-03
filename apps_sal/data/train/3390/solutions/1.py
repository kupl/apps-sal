def narcissistic(value):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)

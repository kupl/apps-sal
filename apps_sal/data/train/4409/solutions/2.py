def noonerize(numbers):
    a, b = numbers
    if not type(a) == int == type(b):
        return "invalid array"
    a, b = map(str, numbers)
    return abs(int(a[0] + b[1:]) - int(b[0] + a[1:]))

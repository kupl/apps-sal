def noonerize(numbers):
    if all((isinstance(x, int) for x in numbers)):
        (a, b) = (str(x) for x in numbers)
        return abs(int(b[0] + a[1:]) - int(a[0] + b[1:]))
    return 'invalid array'

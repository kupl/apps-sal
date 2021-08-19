def noonerize(numbers):
    if not all((isinstance(n, int) for n in numbers)):
        return 'invalid array'
    (a, b) = map(str, numbers)
    return abs(int(a[0] + b[1:]) - int(b[0] + a[1:]))

def noonerize(numbers):

    def spoonerize(numbers):
        (a, b) = [str(n) for n in numbers]
        return '{}{} {}{}'.format(b[0], a[1:], a[0], b[1:])
    if all((isinstance(n, int) for n in numbers)):
        (a, b) = map(int, spoonerize(numbers).split())
        return abs(a - b)
    else:
        return 'invalid array'

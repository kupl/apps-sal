def noonerize(numbers):
    if not all((isinstance(n, int) for n in numbers)):
        return 'invalid array'
    (a, b) = (str(n) for n in numbers)
    return abs(int(f'{b[0]}{a[1:]}') - int(f'{a[0]}{b[1:]}'))

from itertools import count


def reverse_factorial(num):
    for x in count(1):
        if num == x:
            return f'{x}!'
        (num, r) = divmod(num, x)
        if r:
            return 'None'

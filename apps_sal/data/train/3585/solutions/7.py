from functools import reduce


def prod(arr):
    return reduce(lambda x, y: x * y, arr)


def proc_seq(*args):
    args = [set(str(n)) for n in args]
    args[0] -= {'0'}
    minimum = int(''.join((min(n) for n in args)))
    maximum = int(''.join((max(n) for n in args)))
    total = get_total(args)
    number = prod((len(arg) for arg in args))
    return [number, minimum, maximum, total] if number > 1 else [1, minimum]


def get_total(args):
    total = 0
    args = args[::-1]
    for (i, arg) in enumerate(args):
        total += 10 ** i * sum(map(int, arg)) * prod((len(x) for x in args[:i] + args[i + 1:]))
    return total

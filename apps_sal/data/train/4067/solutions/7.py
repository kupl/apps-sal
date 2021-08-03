def iq_test(numbers):
    a = list(map(lambda x: int(x) % 2, numbers.split(' ')))
    return 1 + (a.index(0) if (a.count(0)) == 1 else a.index(1))

def test(number, coffee):
    for i in range(1, 5001):
        if 'dead' in hex(number + i * coffee):
            return i
    return 0


def coffee_limits(year, month, day):
    number = year * 10000 + month * 100 + day
    return [test(number, coffee) for coffee in (0xCAFE, 0xDECAF)]

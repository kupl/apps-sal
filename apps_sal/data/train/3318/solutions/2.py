def number_of_carries(a, b):
    a, b, c, r = [int(x) for x in f"000000{a}"], [int(x) for x in f"000000{b}"], 0, 0
    for x, y in zip(reversed(a), reversed(b)):
        c = x + y + c > 9
        r += c
    return r

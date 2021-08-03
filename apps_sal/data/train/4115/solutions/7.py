def find_outlier(integers):
    assert len(integers) >= 3

    bit = integers[0] & 1

    if integers[1] & 1 != bit:
        return integers[integers[2] & 1 == bit]

    for n in integers:
        if n & 1 != bit:
            return n

    assert False

def order_weight(strng):
    wghts = strng.split()
    srtd = sorted(wghts, key=lambda x: (get_weight(x), x))
    return (' '.join(str(i) for i in srtd))


def get_weight(number):
    return sum(int(digit) for digit in number)

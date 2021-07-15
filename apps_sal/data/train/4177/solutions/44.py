def men_from_boys(arr):
    x = set([a for a in arr if a % 2 == 0])
    y = set([b for b in arr if b % 2 != 0])
    z1 = sorted(y, reverse=True)
    z2 = sorted(x, reverse=False)
    return z2 + z1


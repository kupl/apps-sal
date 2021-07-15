def max_gap(num):
    num.sort()
    return max(b - a for a,b in zip(num, num[1:]))

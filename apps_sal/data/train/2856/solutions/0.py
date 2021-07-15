def gap(num):
    s = bin(num)[2:].strip("0")
    return max(map(len, s.split("1")))

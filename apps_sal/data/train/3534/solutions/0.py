def to_bits(s):
    lst = [0] * 5000
    for i in map(int, s.split()):
        lst[i] = 1
    return lst

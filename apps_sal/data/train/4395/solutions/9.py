def next_higher(value):
    value2 = value + 1
    while bin(value).count('1') != bin(value2).count('1'):
        value2 += 1
    return value2

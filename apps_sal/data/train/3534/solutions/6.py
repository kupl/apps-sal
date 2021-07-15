def to_bits(string):
    numbers = set(int(s) for s in string.split())
    return [(0,1)[n in numbers] for n in range(5000)]


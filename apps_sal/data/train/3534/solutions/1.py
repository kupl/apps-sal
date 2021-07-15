def to_bits(s):
    return [1 if i in set(map(int, s.split("\n"))) else 0 for i in range(5000)]

def to_bits(s): return list(map(set(map(int, s.split('\n'))).__contains__, range(5000)))

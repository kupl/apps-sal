def get_weight(s): return sum(map(ord, filter(str.isalpha, s.swapcase())))

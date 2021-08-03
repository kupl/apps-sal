def countzero(s): return sum((c in "%&B8") * 2 + (c in "abdegopq069DOPQR") * 1 for c in s) + s.count("()")

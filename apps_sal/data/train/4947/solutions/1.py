def sel_number(n, d): return sum(all(d >= int(b) - int(a) > 0for a, b in zip(repr(i), repr(i)[1:]))for i in range(10, n + 1))

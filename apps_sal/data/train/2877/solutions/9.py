def count(a, t, x): return sum((e - t) % x == 0if x != 0else e - t == 0for e in a)

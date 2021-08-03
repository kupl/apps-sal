def is_inertial(a): return a.sort() or (lambda e, o: e > [] < o and max(e[:-1] + [o[0] - 1]) < o[0] <= o[-1] < e[-1])(*[[n for n in a if n % 2 == m]for m in (0, 1)])

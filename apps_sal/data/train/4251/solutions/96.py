def difference_of_squares(n): return (lambda r, s: s(sum(r)) - sum(map(s, r)))(range(1, n + 1), (2).__rpow__)

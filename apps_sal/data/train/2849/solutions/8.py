def peak(a): return sum(sum(a[y + 1:]) == sum(a[:y]) and y for y, _ in enumerate(a)) or -1

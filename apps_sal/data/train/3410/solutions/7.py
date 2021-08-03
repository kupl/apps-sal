def scratch(l): return sum(int(a[3])for a in (r.split()for r in l)if len({*a}) < 3)

def revamp(s): return " ".join(sorted(["".join(sorted(i))for i in s.split()], key=lambda x: (sum(map(ord, x)), len(x), x)))

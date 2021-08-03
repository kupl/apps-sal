def solve(s): return getattr(s, ["lower", "upper"][sum(map(str.isupper, s)) > len(s) // 2])()

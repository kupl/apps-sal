from re import findall
def solve(s): return max(int(m) for m in findall(r"\d+", s))

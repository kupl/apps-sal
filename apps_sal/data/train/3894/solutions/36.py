def solve(s): return s.lower() if (len(list(filter(lambda x: x.islower(),s)))) * 2 >= len(s) else s.upper()

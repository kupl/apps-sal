def trace(m): return None if not m or len(m) != len(m[0]) else sum([m[i][i] for i in range(len(m))])

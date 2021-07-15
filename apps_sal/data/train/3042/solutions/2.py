trace=lambda m: sum(m[i][i] for i in range(len(m))) if m and len(m) == len(m[0]) else None

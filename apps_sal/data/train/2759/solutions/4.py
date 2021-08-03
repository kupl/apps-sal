interleave = lambda *a: [b[i]if len(b) > i else None for i in range(max(len(i)for i in a))for b in a]

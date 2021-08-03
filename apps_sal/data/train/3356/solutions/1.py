def three_amigos(a): return (sorted(((max(a[i:i + 3]) - min(a[i:i + 3]), a[i:i + 3]) for i in range(len(a) - 2) if a[i] % 2 == a[i + 1] % 2 == a[i + 2] % 2), key=lambda x: x[0]) + [(None, [])])[0][1]

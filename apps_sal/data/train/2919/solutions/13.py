def encode(m, k): return [ord(a) - 96 + int(b)for a, b in zip(m, str(k) * 30)]

def find_the_key(s, e): return (lambda l, d: min(int(d[:i])for i in range(l)if(d[:i] * l)[:l] == d))(len(s), ''.join(str(n - ord(c) + 96)for c, n in zip(s, e)))

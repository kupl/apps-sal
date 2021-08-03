def strange_coach(a): return (lambda c: ''.join(k for k in sorted(c)if c[k] > 4) or 'forfeit')(__import__('collections').Counter(w[0]for w in a))

def de_nico(k, m):
    return (lambda k: ''.join(((lambda g: ''.join((g[p] for p in k if p < len(g))))(m[i * len(k):(i + 1) * len(k)]) for i in range(len(m) // len(k) + 1))).strip())((lambda s: [s.index(l) for l in k])(sorted(k)))

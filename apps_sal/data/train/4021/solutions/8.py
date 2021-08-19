def elections_winners(v, k):
    return (lambda m: (lambda c: 0 if c != 1 else c)(v.count(m)) if not k else len([p for p in v if p > m - k]))(max(v))

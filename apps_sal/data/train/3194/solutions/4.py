def berserk_rater(x):
    return (lambda x: 'worstest episode ever' if x < 0 else 'bestest episode ever' if x > 10 else str(x))(sum(map(lambda x: (lambda x: 5 if 'clang' in x else -2 if 'cg' in x else -1)(x.lower()), x)))

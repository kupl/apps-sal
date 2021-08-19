def order(xs):
    return ' '.join(sorted(xs.split(), key=min))

def search(b, p):
    return ','.join((str(i) for i in sorted(p) if i <= b))

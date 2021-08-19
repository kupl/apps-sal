def search(b, p):
    return ','.join(map(str, sorted((c for c in p if c <= b))))

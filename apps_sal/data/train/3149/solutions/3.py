def roof_fix(f, r):
    return all((b not in '\\/' or a == ' ' for (a, b) in zip(f, r)))

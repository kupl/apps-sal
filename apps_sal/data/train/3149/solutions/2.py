def roof_fix(f, r):
    return all((b == ' ' for (a, b) in zip(r, f) if a in '\\//'))

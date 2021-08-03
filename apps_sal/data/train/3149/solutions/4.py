def roof_fix(f, r):
    return all(new == ' ' for old, new in zip(r, f) if old in "\/")

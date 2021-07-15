def roof_fix(f, r):
    return all(x == ' ' or y == '_' for x,y in zip(f, r))

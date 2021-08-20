def roof_fix(f, r):
    return not any([pair[0] in '/\\' and pair[1] != ' ' for pair in zip(r, f)])

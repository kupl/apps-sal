def solve(s):
    upper, lower = [], []

    for w in s:
        if w.isupper():
            upper.append(w)
        else:
            lower.append(w)

    if len(upper) == len(lower) or len(upper) < len(lower):
        return s.lower()
    else:
        return s.upper()

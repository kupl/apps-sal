def solve(s):
    score = 0
    for l in list(s):
        score += 1 if l.isupper() else -1
    return s.upper() if score > 0 else s.lower()


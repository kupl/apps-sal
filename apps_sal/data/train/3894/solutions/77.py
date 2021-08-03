def solve(s):
    upper_count = 0
    lower_count = 0
    for c in s:
        if c.isupper():
            upper_count += 1
        else:
            lower_count += 1
    return s.lower() if lower_count >= upper_count else s.upper()

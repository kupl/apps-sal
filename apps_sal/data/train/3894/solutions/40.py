def solve(s):
    lower_count = 0
    for i in s:
        if i.islower():
            lower_count += 1
    if 2 * lower_count >= len(s):
        return s.lower()
    return s.upper()

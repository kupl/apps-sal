def solve(s):
    (upper, lower, digit, other) = (0, 0, 0, 0)
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        else:
            other += 1
    return [upper, lower, digit, other]

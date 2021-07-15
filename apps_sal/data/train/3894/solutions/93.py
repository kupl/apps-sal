def solve(s):

    lower_count = 0
    for i in range(len(s)):
        if (s[i].islower()):
            lower_count += 1

    upper_count = len(s) - lower_count
    if (lower_count < upper_count):

        return s.upper()

    return s.lower()


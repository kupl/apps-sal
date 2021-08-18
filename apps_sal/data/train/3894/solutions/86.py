def solve(s):
    upper_count = 0
    lower_count = 0
    for letter in s:
        if letter.isupper():
            upper_count += 1
        if letter.islower():
            lower_count += 1
    if upper_count > lower_count:
        return s.upper()
    return s.lower()

def solve(s):
    string = ""
    upper = 0
    lower = 0
    for letters in range(len(s)):
        if s[letters].isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        string += s.upper()
    else:
        string += s.lower()
    return string

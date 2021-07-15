def capitalize(s):
    result = []
    first = ''
    for c in range(len(s)):
        if c % 2 == 0:
            first += s[c].capitalize()
        else:
            first += s[c]
    second = ''
    for c in range(len(s)):
        if c % 2 == 0:
            second += s[c]
        else:
            second += s[c].capitalize()
    return [first, second]

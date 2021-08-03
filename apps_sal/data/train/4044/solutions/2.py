def string_suffix(s):
    length = len(s)
    counter = 0
    for i in range(length):
        for i, c in enumerate(s[i:]):
            if c == s[i]:
                counter += 1
            else:
                break
    return counter

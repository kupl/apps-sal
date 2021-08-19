def solve(s):
    countlow = 0
    countupp = 0
    for letter in s:
        if letter.isupper():
            countupp += 1
        elif letter.islower():
            countlow += 1
    return s.lower() if countlow - countupp >= 0 else s.upper()

def solve(s):
    up = 0
    low = 0

    for letter in s:
        if letter.islower():
            low += 1
        else:
            up += 1

    if low < up:
        return s.upper()
    else:
        return s.lower()

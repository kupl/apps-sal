def solve(s):
    upperS = 0
    lowerS = 0
    for letter in s:
        if letter.islower():
            lowerS += 1
        else:
            upperS += 1
    if upperS > lowerS:
        return s.upper()
    else:
        return s.lower()

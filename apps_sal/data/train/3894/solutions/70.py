def solve(s):
    u = 0
    l = 0
    for letter in s:
        if letter.isupper():
            u += 1
        else:
            l += 1
    if l >= u:
        return s.lower()
    else:
        return s.upper()

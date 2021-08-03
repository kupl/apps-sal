def compare(s1, s2):
    first = 0
    second = 0
    if s1:
        for c in s1:
            if c.isalpha():
                first += ord(c.upper())
            else:
                first = 0
                break
    if s2:
        for j in s2:
            if j.isalpha():
                second += ord(j.upper())
            else:
                second = 0
                break
    return first == second

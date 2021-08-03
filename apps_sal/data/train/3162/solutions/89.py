def compare(s1, s2):
    if s1 is None or not all(map(str.isalpha, s1)):
        x1 = 0
    else:
        x1 = sum(map(ord, s1.upper()))
    if s2 is None or not all(map(str.isalpha, s2)):
        x2 = 0
    else:
        x2 = sum(map(ord, s2.upper()))
    return x1 == x2

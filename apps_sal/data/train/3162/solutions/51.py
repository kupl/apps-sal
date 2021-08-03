def compare(s1, s2):
    n1, n2 = 0, 0
    if s1:
        b1 = any(filter(lambda x: not x.isalpha(), s1))
        n1 = sum(ord(x.upper()) for x in s1) if not b1 else 0
    if s2:
        b2 = any(filter(lambda x: not x.isalpha(), s2))
        n2 = sum(ord(x.upper()) for x in s2) if not b2 else 0
    return n1 == n2

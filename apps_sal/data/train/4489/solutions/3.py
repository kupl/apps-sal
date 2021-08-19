def sum_consecutives(s):
    (n, a) = ([s[0]], s[0])
    for i in range(1, len(s)):
        if s[i] != a:
            n.append(s[i])
            a = s[i]
        elif s[i] == a:
            n[-1] += a
    return n

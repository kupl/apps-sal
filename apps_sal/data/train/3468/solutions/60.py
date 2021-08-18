def scramble(s1, s2):
    j, k = 1, 1
    a = {chr(i): 0 for i in range(97, 123)}
    b = {chr(i): 0 for i in range(97, 123)}
    for i in s1:
        if i not in a:
            continue
        else:
            a[i] = a[i] + 1
    for n in s2:
        if n not in b:
            continue
        else:
            b[n] = b[n] + 1
    for i in s2:
        if a[i] >= b[i]:
            pass
        else:
            return False
    return True

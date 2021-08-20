def scramble(str1, str2):
    if len(str1) < len(str2):
        return False
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    i = 0
    while i < len(str2):
        N = str2.count(str2[i])
        if str1.count(str2[i]) < N:
            return False
        i += N
    return True

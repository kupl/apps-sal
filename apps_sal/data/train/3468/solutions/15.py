def scramble(s1, s2):
    str1 = {}
    str2 = {}
    for s in s1:
        try:
            str1[s] = str1[s] + 1
        except KeyError:
            str1[s] = 1
    for s in s2:
        try:
            str2[s] = str2[s] + 1
        except KeyError:
            str2[s] = 1
    for key in str2:
        try:
            if str1[key] < str2[key]:
                return False
        except KeyError:
            return False
    return True


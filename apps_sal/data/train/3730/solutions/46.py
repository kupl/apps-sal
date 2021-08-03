def capitalize(s):
    s1 = ''
    s2 = ''
    for i in range(0, len(s)):
        to_add = s[i]
        if i % 2 == 0:
            s1 = s1 + to_add.capitalize()
            s2 = s2 + to_add
        else:
            s2 = s2 + to_add.capitalize()
            s1 = s1 + to_add

    return [s1, s2]

    return [s1, s2]

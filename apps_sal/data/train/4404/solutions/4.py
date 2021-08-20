def compare(s1, s2):
    (s1, s2) = (s1.split('.'), s2.split('.'))
    if len(s1) < len(s2):
        s1 += ['0'] * (len(s2) - len(s1))
    elif len(s1) > len(s2):
        s2 += ['0'] * (len(s1) - len(s2))
    for i in range(len(s2)):
        if int(s1[i]) > int(s2[i]):
            return 1
        elif int(s1[i]) < int(s2[i]):
            return -1
    return 0

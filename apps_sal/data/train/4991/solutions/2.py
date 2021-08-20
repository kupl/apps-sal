def mutate_my_strings(s1, s2):
    res = [s1]
    s1 = list(s1)
    s2 = list(s2)
    for (i, x) in enumerate(s1):
        if s1[i] != s2[i]:
            s1[i] = s2[i]
            res.append(''.join(s1))
    return '\n'.join(res) + '\n'

def mutate_my_strings(s1,s2):
    s = s1 + '\n'
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        if s1[i] !=s2[i]:
            s1[i] = s2[i]
            s += "".join(s1) + '\n'
    return(s)

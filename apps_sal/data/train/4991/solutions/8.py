def mutate_my_strings(s1,s2):
    return s1 + '\n' + '\n'.join(s2[:i+1] + s1[i+1:] for i in range(len(s1)) if s1[i] != s2[i]) + '\n' if s1 and s1 != s2 else s1 + '\n'

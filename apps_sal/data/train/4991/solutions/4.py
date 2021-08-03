def mutate_my_strings(s1, s2):
    return '\n'.join([s2[:i] + s1[i:] for i in range(0, len(s1)) if s1[i] != s2[i]] + [s2]) + '\n'

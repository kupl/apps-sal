def mutate_my_strings(s1,s2):
    return '\n'.join(s2[:a] + s1[a:] for a in range(len(s1)) if s2[a] != s1[a]) + '\n' + s2 + '\n' if s1!=s2 else s1 + '\n'

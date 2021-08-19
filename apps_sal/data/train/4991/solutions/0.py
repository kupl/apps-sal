def mutate_my_strings(s1, s2):
    return '\n'.join([s1] + [s2[:i] + s1[i:] for (i, (a, b)) in enumerate(zip(s1, s2), 1) if a != b]) + '\n'

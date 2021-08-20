def mutate_my_strings(s1, s2):
    result = [s1]
    result.extend((f'{s2[:i + 1]}{s1[i + 1:]}' for i in range(len(s1)) if s1[i] != s2[i]))
    result.append('')
    return '\n'.join(result)

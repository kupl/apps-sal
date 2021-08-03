def permutations(s):
    if(len(s) == 1):
        return [s]
    result = []
    for i, v in enumerate(s):
        result += [v + p for p in permutations(s[:i] + s[i + 1:])]
    return list(set(result))

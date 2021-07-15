def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

def capitalize(s):
    return ["".join([s[i].upper() if not (i + k) % 2 else s[i] for i in range(len(s))]) for k in [0, 1]]

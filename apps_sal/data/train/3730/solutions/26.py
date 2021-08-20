def capitalize(s):
    return [''.join((s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s)))), ''.join((s[i].upper() if i % 2 != 0 else s[i] for i in range(len(s))))]

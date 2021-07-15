def capitalize(s):
    cap1 = [s[i].upper() if not i % 2 else s[i] for i in range(len(s))]
    cap2 = [s[i].upper() if i % 2 else s[i] for i in range(len(s))]
    return [''.join(cap1), ''.join(cap2)]



def get_middle(s):
    if len(s) % 2 == 0:
        iA = int(len(s) / 2 - 1)
        iB = int(len(s) / 2 + 1)
        return s[iA:iB]
    else:
        return s[int(len(s) / 2)]

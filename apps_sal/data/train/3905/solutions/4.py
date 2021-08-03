def missing(s):
    for i in range(1, len(s) // 2 + 1):
        save, j, miss = int(s[:i]), i, None
        while j < len(s):
            x, y = str(save + 1), str(save + 2)
            if s[j:].startswith(x):
                j += len(x)
                save = int(x)
            elif s[j:].startswith(y) and miss is None:
                j += len(y)
                save = int(y)
                miss = int(x)
            else:
                miss = None
                break
        if miss is not None:
            return miss
    return -1

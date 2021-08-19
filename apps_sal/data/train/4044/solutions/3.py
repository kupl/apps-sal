def string_suffix(s):
    total = len(s)
    suffixes = [s[y:] for y in range(len(s)) if s[y] == s[0]][1:]
    for suff in suffixes:
        for (y, l) in zip(s, suff):
            if l == y:
                total += 1
            else:
                break
    return total

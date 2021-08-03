def longest(s):
    k = []
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            k.append(s[i])
        else:
            k.append(s[i])
            k.append(' ')
    k += s[-1]
    return max(''.join(k).split(), key=len)

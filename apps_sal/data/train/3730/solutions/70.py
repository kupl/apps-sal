def capitalize(s):
    s = list(s)
    even = []
    for i in range(len(s)):
        if i % 2 == 0:
            even.append(s[i].upper())
        else:
            even.append(s[i])
    even = "".join(even)

    odd = []
    for i in range(len(s)):
        if i % 2 == 0:
            odd.append(s[i])
        else:
            odd.append(s[i].upper())
    odd = "".join(odd)

    return [even, odd]

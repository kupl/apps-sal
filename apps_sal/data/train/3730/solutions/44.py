def capitalize(s):
    first = []
    second = []

    for i in range(len(s)):
        first.append(s[i].upper() if i % 2 == 0 else s[i].lower())

    for j in range(len(s)):
        second.append(s[j].upper() if j % 2 != 0 else s[j].lower())

    return [''.join(first), ''.join(second)]

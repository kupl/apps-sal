def capitalize(s):
    odd = []
    even = []
    for i in range(0, len(s)):
        if i % 2 == 0:
            odd.append(s[i].upper())
        else:
            odd.append(s[i])
    for i in range(0, len(s)):
        if not i % 2 == 0:
            even.append(s[i].upper())
        else:
            even.append(s[i])
    return [''.join(odd), ''.join(even)]

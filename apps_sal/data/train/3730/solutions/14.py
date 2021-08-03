def capitalize(s):
    lst1 = []
    for n in range(0, len(s)):
        if n % 2 == 0:
            lst1.append(s[n].upper())
        else:
            lst1.append(s[n].lower())
    return [''.join(lst1), ''.join(lst1).swapcase()]

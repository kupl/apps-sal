def capitalize(s):
    evens = ''
    odds = ''
    for i in range(0,len(s)):
        if i % 2 == 0:
            evens = evens + s[i].upper()
        else:
            evens = evens + s[i]
    for i in range(0,len(s)):
        if i % 2 == 0:
            odds = odds + s[i]
        else:
            odds = odds + s[i].upper()
    return([evens,odds])

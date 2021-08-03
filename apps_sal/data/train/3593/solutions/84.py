def capitalize(s, ind):
    newstring = []
    for numero in range(len(s)):
        if numero not in ind:
            newstring.append(s[numero])
        elif numero in range(len(s)):
            newstring.append(s[numero].capitalize())
    return "".join(newstring)

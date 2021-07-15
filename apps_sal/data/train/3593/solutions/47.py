def capitalize(s,ind):
#     string = [s[ind] for letter in s if letter]
    result = []
    for i, char in enumerate(s):
        if i in ind:
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

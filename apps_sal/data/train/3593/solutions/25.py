def capitalize(s, ind):
    arr = []
    for i in range(len(s)):
        if i in ind:
            arr.append(s[i].upper())
        else:
            arr.append(s[i])
    return "".join(arr)

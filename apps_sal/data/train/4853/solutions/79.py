def double_char(s):
    s = list(s)
    returnArr = []
    for i in range(len(s)):
        returnArr.append(s[i])
        returnArr.append(s[i])
    return "".join(returnArr)

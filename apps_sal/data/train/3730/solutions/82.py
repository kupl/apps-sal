def capitalize(s):
    result = ""
    for index in range(len(s)):
        if not index % 2:
            result += s[index].upper()
        else:
            result += s[index].lower()
    arr = []
    arr.append(result)
    arr.append(result.swapcase())
    return arr

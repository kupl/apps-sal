def alternateCase(s):
    res = list(s)
    count = 0
    for item in s:
        if item.isalpha():
            if item.isupper():
                res[count] = item.lower()
            else:
                res[count] = item.upper()
        count += 1
    return ''.join(res)

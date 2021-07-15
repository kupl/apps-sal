def lowercase_count(string):
    res = 0
    for i in string:
        if ord(i) > 96 and ord(i) < 123:
            res += 1
    return res

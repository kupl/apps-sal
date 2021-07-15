def uni_total(string):
    res = 0
    for item in string:
        res += ord(item)
    return res

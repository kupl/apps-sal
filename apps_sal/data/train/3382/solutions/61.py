def lowercase_count(s):
    num = 0
    for i in s:
        if i.islower():
            num += 1
    return num

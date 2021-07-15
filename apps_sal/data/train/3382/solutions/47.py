def lowercase_count(string):
    string = str(string)
    a = 0
    for i in string:
        if i.islower():
            a += 1
    return a

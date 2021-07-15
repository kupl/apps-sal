def remove(s):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == "!":
            count += 1
            i += 1
        else:
            i += 1
    i = 0
    s = s.replace("!", "")
    while i < count:
        s += "!"
        i += 1
    return s


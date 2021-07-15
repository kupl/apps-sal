def smash(words):
    s = ""
    for v in words:
        s += v
        if v != words[len(words) - 1]:
            s += " "
    return s

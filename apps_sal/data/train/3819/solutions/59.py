def smash(words):
    out = ""
    if len(words) == 0:
        return ""
    for word in words:
        out += word + " "
    return out[0:-1]

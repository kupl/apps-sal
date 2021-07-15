def remove(s, d):
    for key in d:
        s = s.replace(key, '', d[key])
    return s

def multiple_split(s, delim=[]):
    if not s and (not delim):
        return []
    if not delim:
        return [s]
    for i in delim:
        s = s.replace(i, ' ')
    return s.split()

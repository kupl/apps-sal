def multiple_split(s, d=[]):
    for i in d:
        s = s.replace(i, '___')
    return [x for x in s.split('___') if x]

def string_to_array(s):
    if s is "":
        return [""]
    l = list()
    for i in s.split():
        l.append(i)
    return l

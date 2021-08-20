def string_to_array(s):
    c = []
    for x in s.split():
        c.append(x)
    if len(s) == 0:
        return ['']
    return c

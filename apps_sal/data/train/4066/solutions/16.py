def string_to_array(s):
    result = []
    t = ''
    e = ' '
    for i in s:
        if i not in e:
            t = t + i
        else:
            result.append(t)
            t = ''
    result.append(t)
    return result

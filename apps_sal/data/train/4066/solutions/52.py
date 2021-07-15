def string_to_array(s):
    if len(s) <= 0:
        return ['']
    else:
        l = s.split()
        return list(l)

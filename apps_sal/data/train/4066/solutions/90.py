def string_to_array(s):
    s = str(s)
    if s == '':
        return s.split(',')
    else:
        return s.split()

def string_to_array(s):
    words = []
    if s == '':
        words.append(s)
    else:
        words = s.split()
    return words


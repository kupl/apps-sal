def string_to_array(s):
    if s == '':
        return ['']
    s_list = []
    split_string = s.split()
    for word in split_string:
        s_list.append(word)
    return s_list

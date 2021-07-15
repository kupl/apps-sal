def string_to_array(s):
    if s == '':
        array = ['']
    else:
        array = []
    s = s.split()
    for i in s:
        array.append(i)
    return array

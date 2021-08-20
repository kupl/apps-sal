def string_to_array(s):
    import re
    arr = []
    if s == '':
        arr = ['']
    else:
        pattern = '(\\w+)'
        arr = re.findall(pattern, s)
    return arr

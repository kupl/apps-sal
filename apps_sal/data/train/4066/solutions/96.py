def string_to_array(s):
    arr = []
    if s == '':
        arr = ['']
    else:
        import re
        pattern = '(\w+)'
        arr = re.findall(pattern, s)
    return arr

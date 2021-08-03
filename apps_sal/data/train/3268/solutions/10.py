def words_to_object(s):
    if s == '':
        return '[]'
    for iii in range(s.count(' ')):
        s = s.replace(' ', chr(9), 1)
        s = s.replace(' ', chr(10), 1)
    s_list_a = s.split(chr(10))
    retval_list = []
    for val in s_list_a:
        zname, zid = val.split(chr(9))
        retval_list.append('''{name : ''' + chr(39) + zname + chr(39) + ''', id : ''' + chr(39) + zid + chr(39))
    retval = '''[''' + '}, '.join(retval_list) + '''}]'''
    return retval

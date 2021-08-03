def words_to_object(s):
    ss = s.split()
    return '[' + ', '.join(['{' + 'name : \'{0}\', id : \'{1}\''.format(ss[i * 2], ss[i * 2 + 1]) + '}' for i in range(len(ss) // 2)]) + ']'

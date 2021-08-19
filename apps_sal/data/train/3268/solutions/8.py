def words_to_object(s):
    if not s:
        return '[]'
    s = s.split()
    s = [(s[i], s[i + 1]) for i in range(0, len(s), 2)]
    s = ["{{name : '{}', id : '{}'}}".format(i[0], i[1]) for i in s]
    return '[' + ', '.join(s) + ']'

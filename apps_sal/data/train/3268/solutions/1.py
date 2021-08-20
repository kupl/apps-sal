def words_to_object(s):
    return '[' + ', '.join(("{name : '%s', id : '%s'}" % (n, i) for (n, i) in zip(s.split()[::2], s.split()[1::2]))) + ']'

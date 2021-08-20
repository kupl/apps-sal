def words_to_object(s):
    return '[' + ', '.join(("{name : '%s', id : '%s'}" % t for t in zip(*[iter(s.split())] * 2))) + ']'

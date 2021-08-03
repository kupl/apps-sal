objectify = "{{name : '{}', id : '{}'}}".format


def words_to_object(s):
    pairs = zip(*[iter(s.split())] * 2)
    obj_list = ', '.join(objectify(*pair) for pair in pairs)
    return '[{}]'.format(obj_list)

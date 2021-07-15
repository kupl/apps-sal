def words_to_object(s):
    xs = s.split()
    return '[{}]'.format(', '.join(f"{{name : {name!r}, id : {id_!r}}}" for name, id_ in zip(xs[::2], xs[1::2])))

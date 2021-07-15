def string_to_array(s):
    if len(s) == 0:
        _list = []
        _list.append('')
        return _list
    return list(s.split())

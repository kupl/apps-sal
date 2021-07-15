def denumerate(enum_list):
    if not isinstance(enum_list, list):
        return False
    for el in enum_list:
        if not isinstance(el, tuple):
            return False
        if len(el) != 2:
            return False
        if not isinstance(el[1], str):
            return False
        if len(el[1]) != 1:
            return False
        if not el[1].isalnum():
            return False
        if not (0 <= el[0] <= len(enum_list) - 1):
            return False
    return  ''.join(tup[1] for tup in sorted(enum_list))

def who_is_paying(name):
    if len(name) > 2:
        tup1 = [name, name[:2]]
        return tup1
    else:
        tup2 = [name]
        return tup2

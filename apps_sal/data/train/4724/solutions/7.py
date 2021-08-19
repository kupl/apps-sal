def drop_cap(str_):
    return ' '.join(map(lambda x: x.title() if len(x) > 2 else x, str_.split(' ')))

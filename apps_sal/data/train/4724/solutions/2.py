def drop_cap(str_):
    return ' '.join([i[0].upper() + i[1:].lower() if len(i) > 2 else i for i in str_.split(' ')])

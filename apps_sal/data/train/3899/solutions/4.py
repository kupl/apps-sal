def guess_my_number(a, b='123-451-2345'):
    a = set(a + '-')
    return ''.join(('#' if x not in a else x for x in b))

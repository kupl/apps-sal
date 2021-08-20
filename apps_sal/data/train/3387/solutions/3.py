from re import search


def name_in_str(s, n):
    return search('.*'.join(list(n)), s, 2) != None

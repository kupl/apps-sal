import string


def lowercase_count(string):
    return len([x for x in string if x in 'abcdefghijklmnopqrstuvwxyz'])

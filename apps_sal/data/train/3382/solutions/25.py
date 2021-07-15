def lowercase_count(strng):
    import string
    return len(''.join([i for i in strng if i in string.ascii_lowercase]))

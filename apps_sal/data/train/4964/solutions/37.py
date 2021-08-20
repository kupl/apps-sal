import string as str


def is_uppercase(inp):
    res = str.ascii_uppercase + ' '
    ret = ' '
    for i in inp:
        if i in res or i in str.punctuation or i in str.digits:
            ret = True
        else:
            ret = False
            break
    return ret

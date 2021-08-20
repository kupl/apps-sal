from re import sub


def err_bob(string):
    string = sub('\\b(\\w*[bcdfghjklmnpqrstvwxyz])\\b', '\\1err', string)
    return sub('\\b(\\w*[BCDFGHJKLMNPQRSTVWXYZ])\\b', '\\1ERR', string)

from re import sub


def err_bob(string):

    string = sub(r'\b(\w*[bcdfghjklmnpqrstvwxyz])\b', r'\1err', string)
    return sub(r'\b(\w*[BCDFGHJKLMNPQRSTVWXYZ])\b', r'\1ERR', string)

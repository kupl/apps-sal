from re import sub

def replace_dashes_as_one(s):
    return sub("-[\s-]*-", '-', s)

def is_lock_ness_monster(s):
    return any(map(lambda x:x in s, ('tree fiddy','three fifty','3.50')))

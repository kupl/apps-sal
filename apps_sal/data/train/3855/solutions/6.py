def is_lock_ness_monster(string):
    return any(1 for x in ["3.50", "tree fiddy", "three fifty"] if x in string)

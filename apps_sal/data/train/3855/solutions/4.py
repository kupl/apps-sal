def is_lock_ness_monster(string):
    check = "3.50"
    check2 = "three fifty"
    check3 = "tree fiddy"
    return ((check in string) or (check2 in string) or (check3 in string))

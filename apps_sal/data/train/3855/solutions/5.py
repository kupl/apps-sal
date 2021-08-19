def is_lock_ness_monster(string):
    import re
    return bool(re.findall('(?:tree fiddy|3\\.50|three fifty)', string))

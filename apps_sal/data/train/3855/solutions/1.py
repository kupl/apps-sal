import re

def is_lock_ness_monster(s):
    return bool(re.search(r"3\.50|tree fiddy|three fifty", s))

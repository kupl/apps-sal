import re
def is_lock_ness_monster(string):
    return bool(re.search(r'three fifty|tree fiddy|3\.50', string))

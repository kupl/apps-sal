def is_lock_ness_monster(phrase):
    PATTERNS = ('tree fiddy', '3.50', 'three fifty')
    return any(pattern in phrase for pattern in PATTERNS)

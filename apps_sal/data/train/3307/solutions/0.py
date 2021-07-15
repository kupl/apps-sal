def fat_fingers(s):
    if not s: return s
    swap = [False]
    return ''.join( c.swapcase() if swap[0] else c for c in s 
                    if c not in "aA" or swap.__setitem__(0, not swap[0]) )

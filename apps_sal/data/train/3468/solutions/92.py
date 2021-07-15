def map_char_count(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def scramble(s1, s2):
    s1_count = map_char_count(s1)
    s2_count = map_char_count(s2)
    for k, v in list(s2_count.items()):
        if k not in s1_count or s1_count[k] < v:
            return False
    return True
    


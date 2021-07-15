def longest(s1, s2):
    new_str = ''.join([s1,s2])
    s = list(new_str)
    s = list(set(s))
    s.sort()
    result = ''.join(s)
    return result
    


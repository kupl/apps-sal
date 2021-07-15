def increment_string(strng):
    s1 = strng.rstrip('0123456789')
    s2 = strng[len(s1):]
    if s2 == '': return strng+'1'
    return s1 + str(int(s2)+1).zfill(len(s2))

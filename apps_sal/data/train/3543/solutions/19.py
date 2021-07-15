def increment_string(strng):
    import re
    match = re.search(r'\d+$', strng)
    if match:
        s = match.group()
        s1 = strng[:len(strng)-len(s)] + str.rjust(str(int(s)+1), len(s), '0')
    else:
        s1 = strng+'1'
    return s1

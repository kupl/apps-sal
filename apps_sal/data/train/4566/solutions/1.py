def counting_valleys(s): 
    last_level = level = 0
    c = 0
    for m in s:
        if m == 'F':
            continue
        level += (-1, 1)[m == 'U']
        if last_level < level == 0:
            c += 1
        last_level = level
    return c

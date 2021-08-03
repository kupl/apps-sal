def counting_valleys(s):
    level = 0
    in_valley = False
    count = 0
    for c in s:
        if c == 'U':
            level += 1
        elif c == 'D':
            level -= 1
        if level >= 0 and in_valley:
            count += 1
        in_valley = level < 0
    return count

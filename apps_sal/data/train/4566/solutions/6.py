def counting_valleys(s):
    res = current = 0
    for c in s:
        if c == 'U':
            current += 1
            if current == 0:
                res += 1
        elif c == 'D':
            current -= 1
    return res

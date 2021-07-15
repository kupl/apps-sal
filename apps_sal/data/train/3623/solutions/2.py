def product(s):
    ce = cq = 0
    for i in s:
        if i == '!':
            ce += 1
        elif i == '?':
            cq += 1
    return ce * cq

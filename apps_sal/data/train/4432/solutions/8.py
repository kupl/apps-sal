def can_jump(lst):
    p, l = lst[0], len(lst)
    if l == 1:
        return False
    if p >= l:
        return True
    for i in range(1, p+1):
        if lst[i] and can_jump(lst[i:]):
            return True
    return False

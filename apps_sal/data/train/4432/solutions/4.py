def can_jump(lst):
    l = len(lst)
    for i in range(l - 2, -1, -1):
        if lst[i] >= l - i:
            l = i
    return l == 0

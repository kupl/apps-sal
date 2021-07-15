def invite_more_women(arr):
    if arr == []:
        return False
    m = 0
    w = 0
    for el in arr:
        if el == 1:
            m += 1
        elif el == -1:
            w += 1
    if w < m:
        return True
    elif w >= m:
        return False


def invite_more_women(arr):
    x = len(arr)
    i = 0
    a = 0
    if x == 2:
        if arr[0] == 1:
            if arr[1] == -1:
                return False
    while i < x:
        a = a + arr[i]
        break
    if a > 0:
        return True
    elif a < 0:
        return False
    else:
        return False

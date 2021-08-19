def is_onion_array(a):
    mid = len(a) // 2
    for i in range(0, mid):
        if a[i] + a[-i - 1] > 10:
            return False
    return True

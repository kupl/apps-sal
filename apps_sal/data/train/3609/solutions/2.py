def is_onion_array(a):
    for i in range(0, len(a) // 2):
        if a[i] + a[-i - 1] > 10:
            return False
    return True

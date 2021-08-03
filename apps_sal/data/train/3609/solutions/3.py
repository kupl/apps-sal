def is_onion_array(a):
    l = len(a)
    return all(a[i] + a[l - i - 1] <= 10 for i in range(l // 2))

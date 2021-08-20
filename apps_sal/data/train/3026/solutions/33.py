def min_value(digits):
    set_n = set()
    for i in digits:
        set_n.add(i)
    arr = []
    for i in set_n:
        arr.append(str(i))
    arr = sorted(arr)
    return int(''.join(arr))

def count_positives_sum_negatives(arr):
    # acoder! solution

    p = 0
    n = 0
    # especial case ([]),[])
    if arr == []:
        return []

    for i in arr:
        if i != 0:
            if i > 0:
                p += 1
            else:
                n += i

    # especial case ([0,0,0,0,0,0,0,0,0]),[0,0])
    if p == 0 and n == 0:
        return [0, 0]

    return [p, n]

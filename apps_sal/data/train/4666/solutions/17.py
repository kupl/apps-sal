def array_plus_array(arr1, arr2):
    total1 = 0
    total2 = 0
    for a in arr1:
        total1 += a

    for b in arr2:
        total2 += b

    total = total1 + total2
    return total

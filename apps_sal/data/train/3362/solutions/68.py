def sum_mix(arr):
    s=0
    for ele in arr:
        if ele is not int:
            ele=int(ele)
            s+=ele
    return s

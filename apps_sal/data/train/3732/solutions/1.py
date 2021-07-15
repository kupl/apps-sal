def is_madhav_array(arr):
    p = 1
    c = 2
    while p < len(arr) and arr[0] == sum(arr[p:p + c]):
        p += c
        c += 1      
    return p == len(arr) > 1

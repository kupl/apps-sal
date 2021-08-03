def sum_array(arr):
    if arr == None or arr == []:
        return 0
    mi = min(arr)
    ma = max(arr)
    st = (arr.count(mi) - 1) * mi + (arr.count(ma) - 1) * ma
    for i in arr:
        if i not in [mi, ma]:
            st += i
    return st
    # your code here

def count_adjacent_pairs(st):
    if not st:
        return 0
    res = 0
    arr = [i.lower() for i in st.split()]
    for i in range(len(arr)-1):
        if i == 0:
            if arr[i] == arr[i+1]:
                res += 1
        elif arr[i] == arr[i+1] != arr[i-1]:
            res += 1
    return res

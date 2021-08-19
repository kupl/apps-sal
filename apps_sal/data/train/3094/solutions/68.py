def sum_array(arr):
    if arr == [] or arr == None:
        return 0
    elif len(arr) > 2:
        return sum(sorted(arr)[1:-1])
    else:
        return 0
    #sum(i for i in arr if i > min(arr) and i < max(arr))

def sum_array(arr):
    if arr == None:
        return 0
    elif arr == []:
        return 0
    else:
        a = max(arr)
        b = min(arr)
        print(a)
        arr.remove(a)
        if arr == []:
            return 0
        else:
            total = 0
            arr.remove(b)
            for i in arr:
                total += i
            return total

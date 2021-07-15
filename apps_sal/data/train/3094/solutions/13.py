def sum_array(arr):
    if arr == [] or arr == None or len(arr) <= 2:
        return 0
    else:
        sum = 0
        arr.sort(reverse=False)
        for i in arr:
            sum += i
        return sum - int(arr[0]+arr[-1])

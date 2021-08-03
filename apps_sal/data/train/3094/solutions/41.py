def sum_array(arr):
    if arr == None or arr == [] or len(arr) < 2:
        return 0
    else:
        lowest = arr[0]
        for i in arr:
            if i < lowest:
                lowest = i
        highest = arr[0]
        for i in arr:
            if i > highest:
                highest = i
        tot = 0
        for i in arr:
            tot += i
        return tot - lowest - highest

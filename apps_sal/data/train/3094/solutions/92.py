def sum_array(arr):
    if arr == None or arr == []:
        return 0
    for x in arr:
        if int(len(arr)) >= 3:
            return int(sum(arr) - min(arr) - max(arr))
        else:
            return 0

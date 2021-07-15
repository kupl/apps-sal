def elements_sum(arr, d=0):
    count = len(arr)    
    result = 0
    for i in arr:
        if len(i) >= count:
            result += i[count-1]
        else:
            result += d
        count -= 1
    return result

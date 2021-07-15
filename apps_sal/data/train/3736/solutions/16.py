def minimum(arr):
    lowest_num = 999999999999999
    for x in arr:
        if x < lowest_num:
            lowest_num = x
    return lowest_num     
def maximum(arr):
    highest_num = 0
    for x in arr:
        if x > highest_num:
            highest_num = x
    return highest_num        

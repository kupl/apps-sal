def minimum(arr):
    num = None
    for i in arr:   
        if not num:
            num = i
        elif i < num:
            num = i
    return num

def maximum(arr):
    num = 0
    for i in arr:
        if i > num:
            num = i
    return num

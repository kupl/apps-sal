def db_sort(arr):
    num = []
    alpha = []
    
    for i in arr:
        if isinstance(i, int):
            num.append(int(i))
        else:
            alpha.append(i)
            
    num.sort()
    alpha.sort()
    
    return num + alpha

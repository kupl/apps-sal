def first_non_consecutive(arr):
    x = len(arr)
    z= []
    y = []
    for k in range(0,x-1):
        if (arr[k]+1) == arr[(k+1)]:
            y.append(arr[k+1])
        else:
            z.append(arr[k+1])
    
    if z==[]:
        return None
    else:
        z = min(z)
        return z
            


    #your code here


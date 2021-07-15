def even_numbers(arr,n):
    x=[]
    for i in arr[::-1]:
        if len(x)<n and i%2 ==0:
            x.append(i) 
        else:
            pass
    return  x[::-1]

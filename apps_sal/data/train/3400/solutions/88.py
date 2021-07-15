def even_numbers(arr,n):
    res=[]
    for i in arr[::-1]:
        if n==0:
            break
        if i%2==0:
            res.append(i)
            n-=1
    return res[::-1]

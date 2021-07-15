def even_numbers(arr,n):
    res=[]
    for i in range(1,len(arr)+1):
        if arr[-i]%2==0:
            res.append(arr[-i])
            if len(res)==n:
                break
        
    return res[::-1]


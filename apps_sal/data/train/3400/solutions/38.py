def even_numbers(arr,n):
    res = [i for i in arr if i%2==0]
    while len(res)>n:
        res.pop(0)
    return res

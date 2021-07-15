def explode(arr):  
    num=sum([i for i in arr if  type(i)==int])
    return 'Void!' if not num else [ arr for i in range(num) ]

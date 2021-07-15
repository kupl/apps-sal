def even_numbers(arr,n):
    even_count=0
    result=[]
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i]%2==0:
            result.insert(0,arr[i])
            even_count+=1
        if even_count==n:
            break
            
    return result
    
            
    


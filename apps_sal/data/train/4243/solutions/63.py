def find_average(arr):
    sum=0
    
    if 0==len(arr):
        return 0;
    
    for num in arr:
        sum+=num
        
    sum=sum/len(arr)
    
    return sum

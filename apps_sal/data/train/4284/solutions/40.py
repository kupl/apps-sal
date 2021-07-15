def array_leaders(numbers):
    
    re=[]
    for i in range(0,len(numbers)):
        if numbers[i]>sum(numbers[i+1:]):
            re.append(numbers[i])
    return re

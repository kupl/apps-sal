def is_odd_heavy(arr):
    is_odd= False
    for index in range(len(arr)-1):
        if(sorted(arr)[index]%2==1)and(sorted(arr)[index+1]%2==0):
            return False
        if(sorted(arr)[index]%2==1)or(sorted(arr)[index+1]%2==1):
            is_odd= True
    return is_odd if len(arr)!=1 else (arr[0]%2==1)


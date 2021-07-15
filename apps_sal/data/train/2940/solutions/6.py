def repeats(arr):
    
    
    return sum(filter(lambda num : arr.count(num) == 1, arr))

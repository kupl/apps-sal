def sum_mix(arr):
    total = 0
    for num in arr:
        if type(num) == str:
            total += int(num)
        else: 
            total += num
        
    return total

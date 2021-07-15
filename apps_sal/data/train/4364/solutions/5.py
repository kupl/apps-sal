def odd_or_even(arr):
    sum = 0
    answer = ""
    
    for el in arr:
        sum += el
    
    if sum % 2 == 0:
        answer = "even"
    else:
        answer = "odd"
    
    return answer

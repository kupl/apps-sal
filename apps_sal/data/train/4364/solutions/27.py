def odd_or_even(arr):
    sum = 0
    for X in arr:
        sum = sum + X
        remainder = sum % 2
    if remainder == 0:
        return "even"
        
    else:
        return "odd"


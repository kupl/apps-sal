def odd_or_even(arr):
    sumOfNums = sum(arr)
    
    if sumOfNums % 2 == 0:
        return 'even'
    else:
        return 'odd'

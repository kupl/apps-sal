def odd_or_even(arr):
    zum = 0
    for i in arr:
        zum += i
    if(zum%2== 0):
        return "even"
    else:
        return "odd"

def odd_or_even(arr):
    var = 0
    for i in arr:
        var = i + var
        
    if var % 2 == 0:
        return("even")
    else:
        return("odd")

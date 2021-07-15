def odd_or_even(arr):
    thesum = 0
    for i in arr:
        thesum +=i
    if thesum %2==0:
        return 'even'
    else:
        return 'odd'

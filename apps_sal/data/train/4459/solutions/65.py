def nth_even(n):
    return list(range(0, n*2+1, 2))[n-1]
    #Makes a list of numbers that start at zero, increment
    #by 2, and stops at n*2. The index is one less than
    #the position requested.


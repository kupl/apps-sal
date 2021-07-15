def odd_count(n):
    #Return number of positive odd numbers below N
    #Find numbers below N -> Add +1 to count 
    #More of a math problem
    #Try to find a way besides checking every individual integer.
    
    return(n // 2)
    
    """
    Look at the top of the range: if it is odd then add 1, if even leave alone.

Look at the bottom of the range: if it is odd then subtract 1, if even leave alone.

Take the difference between the new even top and bottom; then divide by two.

So for the range [1,100] you get 100−02=50 odd integers.
"""

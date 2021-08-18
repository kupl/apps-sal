def odd_count(n):

    return(n // 2)

    """
    Look at the top of the range: if it is odd then add 1, if even leave alone.

Look at the bottom of the range: if it is odd then subtract 1, if even leave alone.

Take the difference between the new even top and bottom; then divide by two.

So for the range [1,100] you get 100−02=50 odd integers.
"""

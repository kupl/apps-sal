def get_participants(handshakes):
    from math import ceil

    """
        Person 
        can shake hands with (n-2) people... etc. Therefore,
        n people can at most shake hands h = n*(n-1)/2 different times.
        
        If we flip this equation we get the amount
        of people necessary:
        n = 1/2 +(-) sqrt((8*h + 1)/4)
        
        The number of handshakes given might be smaller than
        the max amount possible for n people, so we need to round up.
    """

    return ceil(0.5 + ((8 * handshakes + 1) / 4)**0.5)

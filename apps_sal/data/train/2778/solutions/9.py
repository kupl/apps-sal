def faro_cycles(deck_size):
    """
        If the deck size is 2*n, then it'll take at least
        k shuffles to get back to the starting order, where k 
        is the smallest integer such that 2**k = 1 (mod 2*n - 1)
    """
    
    if deck_size <= 2: return 1
    
    k = 1
    while ((2**k % (deck_size - 1)) != 1): k += 1
    return k

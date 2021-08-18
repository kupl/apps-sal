def over_the_road(address, n):
    '''
    Input: address (int, your house number), n (int, length of road in houses) 
    Returns: int, number of the house across from your house. 
    '''
    return (2 * n + 1 - address)

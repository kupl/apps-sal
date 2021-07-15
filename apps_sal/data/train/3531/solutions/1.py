def valid_mersenne(n):
    '''Currently using the Lucas-Lehmer test.'''
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    mersenne = 2**n - 1
    
    residue = 4
    for _ in range(n - 2):
        residue = (residue * residue - 2) % mersenne
    
    return not residue

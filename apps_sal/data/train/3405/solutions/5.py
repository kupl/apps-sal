from math import *

def pow_root_pandigit(val, n, k):
    '''
    Create a function to give k smaller couples of the root - pandigital numbers with the power n
    and bigger than val.
    '''
    # Create the empty list to return
    l = []
    # Put the value to zero
    if val < 0:
        val = 0
    # Case where val is bigger than the bigger pandigital number
    if val > 987654321:
        return l
    r = 1./n
    # Look for all the powers bigger than val and stop when it reach the len of the list or the
    # end of the possibility
    for i in range(int(ceil(((val+1) ** r))), int(987654322 ** r)):
        string = str(i ** n)
        if len(set(string)) == len(string) and '0' not in string and '0' not in str(i) and len(set(str(i))) == len(str(i)): 
            l.append([i, int(string)])
        if len(l) == k : break
    # Check if only one element
    if len(l) == 1:
        l = l[0]
    return l
    


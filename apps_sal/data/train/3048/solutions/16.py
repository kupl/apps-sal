def alternateCase(s):
    #return s.swapcase() python's swapcase
    my_own_swapcase = lambda w: ''.join([l.lower() if l.isupper() else l.upper() if l.islower() else l for l in w])
    return my_own_swapcase(s)

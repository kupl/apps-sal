def automorphic(n):
    return ( "Not!!", "Automorphic")[int( str(n**2)[-len( str(n) ):] ) == n]

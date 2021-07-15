def tidyNumber(n):
    return True if  all( [ front <= behind for front, behind in zip( str( n), str( n)[ 1:])]) else False

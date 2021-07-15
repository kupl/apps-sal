def max_number(n):
    y= sorted([ x for x in str(n)])
    return int( "".join(x for x in y)[::-1] )


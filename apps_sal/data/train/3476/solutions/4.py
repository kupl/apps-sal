def unlucky_number(n):
    return sum( 1 for n in range(0,n+1,13) if set(str(n)) & set('47') == set() )

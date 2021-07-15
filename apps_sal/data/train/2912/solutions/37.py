def find_multiples(integer, limit):
    # inserts all elements from integer to limit incremented by integer
    a = list(range(integer,limit + 1,integer))
    return a
    
find_multiples(5,25)

# from more_itertools import unique_everseen as distinct

from itertools import filterfalse

def unique_everseen(iterable):
    seen = set()
    seen_add = seen.add
    for element in filterfalse(seen.__contains__, iterable):
        seen_add(element)
        yield element
        
distinct = lambda arr: list(unique_everseen(arr))   
        


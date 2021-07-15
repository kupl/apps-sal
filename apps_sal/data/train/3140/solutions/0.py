def is_happy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum( int(d)**2 for d in str(n) )
    return n == 1


def happy_numbers(n):    
    return [x for x in range(1, n+1) if is_happy(x)]

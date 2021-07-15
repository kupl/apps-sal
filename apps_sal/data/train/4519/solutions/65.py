def max_number(n):
    n=[ i for i in str(n)]
    n.sort(reverse=True)
    return int(''.join(n))

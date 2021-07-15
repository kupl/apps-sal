def reverse_number(n):
    n=str(n)
    l=len(n)
    if n[0]=='-':
        n=int(n[:l*-1:-1])*-1
    else: n=n[::-1]
    return int(n)

def arithmetic_sequence_sum(a, r, n):
    b=a
    x=n-1
    while x!=0:
        a+=r
        x-=1
    return (n*(b+a))/2

def row_sum_odd_numbers(n):
    a=0
    o=0
    e=0
    for x in range(1,n+1):
        a+=x
    for y in range(1,2*a,2):
        o+=y
    for z in range(1,2*(a-n),2):
        e+=z
    return o-e

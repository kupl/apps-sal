def hollow_triangle(n):
    if n == 1:
        return ['#']
    first = ["_"*(n-1)+"#"+"_"*(n-1)]
    last = ["#"*(2*n-1)]
    return first +["_"*(n-i-1)+"#"+"_"*(2*i-1)+"#"+"_"*(n-i-1) for i in range(1,n-1)] + last

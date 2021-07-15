def difference_of_squares(n):
    s1=(1+n)/2*n
    s2=0
    for i in range(1,n+1):
        s2+=i**2
    return abs(s2-s1**2)

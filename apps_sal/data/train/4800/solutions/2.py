def hotpo(n):
    def even_odd(m):
        return [3*m+1, m/2][m%2==0]
    c = 0
    while n!=1:
        n =  even_odd(n)
        c+=1
    return c

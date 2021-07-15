def squares(x, n):
    fun = lambda x,n: x if n <= 1 else fun(x, n-1) ** 2
    return [fun(x, i) for i in range(1, n+1)]
    
    
    


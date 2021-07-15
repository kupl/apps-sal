A = lambda x,n: x * (((n-1) // x) * ((n-1) // x + 1)) // 2
solution=lambda n:A(3,n) + A(5,n) - A(15,n)

sumin = lambda n: n * (n + 1) * (2 * n + 1) // 6
    
sumax = lambda n: n * (n + 1) * (4 * n - 1) // 6
    
sumsum = lambda n: sumin(n) + sumax(n)

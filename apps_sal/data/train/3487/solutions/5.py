def beeramid(bonus, price):
    b = bonus/price; n = 1
    while True:
        if b < n*(n+1)*(2*n+1)/6: 
            return n-1; break
        n += 1


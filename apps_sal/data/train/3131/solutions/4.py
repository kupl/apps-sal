def digits(n):
    p = 1
    m = n
    while n:
        p *= n % 10
        n //= 10
    return m if m < 10 else p
         
def unique_digit_products(a):
    return len(set([digits(i) for i in a]))

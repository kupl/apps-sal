def f(n, v):
    # Removes remainders from Calculation
    #     Technically not doing this will still work 
    #     in python 2 but I considered it to be bad 
    #     practice, so I changed it.
    return n / v - (n % v) / v
    
def cheapest_quote(n):
    # Pattern max 4:
    #     n*.1 (solution without 'discounts')
    #   Subtract sum of total by sum of discount:
    #     divide by 5 and then 2 (repeat) until 1;
    #     multply by .01 (change to fraction).
    #   Simplified n/5/2 to n/10 and so on.
    return round(n*.1-(f(n, 5)+f(n, 10)+f(n, 20)+f(n, 40))*.01, 2)

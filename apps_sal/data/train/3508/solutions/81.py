def halving_sum(n): 
    # your code here
    b=1
    top=0
    while b<=n:
        top+=int(n/b)
        b*=2
    return top

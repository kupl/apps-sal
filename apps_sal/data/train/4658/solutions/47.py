def max_product(lst,n):
    ans = 1
    for i in sorted(lst,reverse = True)[:n]:
        ans *= i
    return ans 

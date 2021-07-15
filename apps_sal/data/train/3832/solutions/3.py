def f(n):
    #by working through sizes 1-9 found an iterative relationship
    #f(1) = 0
    #f(n) = n*f(n-1) + (1 if n is even else -1)
    if (n==0):
        return 1
    else:
        return n*f(n-1)+(1 if n%2==0 else -1)

def all_permuted(array_length):
    return f(array_length)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def padovan(n):
    if n==0 or n==1 or n==2:
        return 1
    else:
        return padovan(n-2)+padovan(n-3)
        
padovan=memoize(padovan)

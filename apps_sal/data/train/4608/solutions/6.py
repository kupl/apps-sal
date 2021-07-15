def finance(n):
    return sum([sum(range(2*i,i+n+1)) for i in range(n+1)])

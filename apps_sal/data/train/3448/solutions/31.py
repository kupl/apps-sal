def f(n):
    if isinstance(n, int) and n > 0:
        nn = [i for i in range(n + 1)]
        return sum(nn)

#    sum = 0
#    if isinstance(n, int):
#        if n > 0:
#            for i in range(n+1):
#                sum += i
#            return sum
#        return None
#    else:
#        return None

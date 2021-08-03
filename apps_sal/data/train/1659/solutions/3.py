def exp_sum(n, x=None, maxx=None, dic={}):
    x, maxx = (n, n) if x == None else (x, maxx)
    return sum([dic[(x - i, i)] if (x - i, i) in dic else(0 if dic.update({(x - i, i): exp_sum(n, x - i, i, dic)}) else dic[(x - i, i)])for i in range(1, min([maxx, x]) + 1)[::-1]]) if x else 1

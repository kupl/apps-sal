def mango(q, p):
    return sum(map(lambda x,y: x*y, [q//3, q%3],[2*p, p]))

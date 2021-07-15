from itertools import count

def primeFactors(n):
    def power(x, n, res=""):
        i = 0
        while not n%x: n, i = n//x, i+1
        return n, res+(f"({x})" if i==1 else f"({x}**{i})" if i>1 else "")
    n, res = power(2, n)
    for x in count(3, 2):
        if n == 1: return res
        n, res = power(x, n, res)

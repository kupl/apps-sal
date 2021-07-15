from math import factorial as fact

def combinations(n, k):
    return fact(n) // (fact(k) * fact(n-k))

def checkchoose(posters, colors):
    return min([k for k in range(colors//2 +1) if combinations(colors, k) == posters], default=-1)

def solution(a, b):
    k = sorted([a, b], key=len)
    print(k)
    g = k[0] + k[1] + k[0]
    return g

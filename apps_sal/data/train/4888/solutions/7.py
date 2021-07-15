def recaman(n):
    a, i = 0, 0
    k = {0}
    while i<=n:
        x = [a+i,a-i][(a-i) > 0 and a-i not in k]
        k.add(x)
        a = x
        i += 1
    return x      

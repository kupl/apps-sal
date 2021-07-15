
def fusc(n):
    f = [0, 1]
    for i in range(1, n + 1):
        f.append(f[i])
        f.append(f[i] + f[i+1])    
    return f[n]

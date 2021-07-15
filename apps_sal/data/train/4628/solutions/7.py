d = {0: lambda x: x,
     1: lambda x: 1, 
     2: lambda x: (x // 4) * 4 + 3, 
     3: lambda x: 0}

def sxore(n):
    return d[n % 4](n)

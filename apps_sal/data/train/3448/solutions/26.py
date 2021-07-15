def f(n):
    try:
        x = int(n)
        if int(n) < 0:
            return None
        elif int(n) > 0:
            return sum([i for i in range(0, n+1)])
        
    except:
        None

def pattern(n):
    
    x = ""
    
    for i in range(1, n+1):
        x += str(i) * i + "\n"
    
    print (x)
    return x.strip()

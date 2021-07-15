def pattern(n):
    s = ''; 
    for i in range(1, n+1):
        for j in range(1, i+1):
            s = s + str(i)
        if i < n:
            s = s + "\n"
    return s

def powers_of_two(n):
    a = [1]
    if n == 0:
        return a
    else:
        for i in range(1,n+1):
            a.append(2**i)  
    return a

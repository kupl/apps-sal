def multiples(m, n):
    # Implement me! :)
    a = [n]
    i = 2
    l = n
    while m != 1:
        n = l
        n *= i
        a.append(n)
        m -= 1
        i += 1
        
    return a

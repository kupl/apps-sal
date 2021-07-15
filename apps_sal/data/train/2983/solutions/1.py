def bouncy_count(n):
    k = m = 1
    for i in range(1, 11):
        k *= n + i*(1+(i == 10))
        m *= i
    return 10*(10**(n-1)+n)- k // m + 1

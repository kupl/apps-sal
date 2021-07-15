def powers_of_two(n):
    s=1
    a=[1]
    for i in range(n):
        s*=2
        a.append(s)
    return(a)

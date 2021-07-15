def multiples(m, n):
    print(m)
    print(n)
    list1 = []
    i = 1
    while i <= m:
        multi = n * i
        print(multi)
        list1.append(multi)
        
        i += 1
    print(list1)
    return(list1)

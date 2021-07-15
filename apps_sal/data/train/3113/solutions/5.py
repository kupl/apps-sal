def distribute(m, n):
    list = []
    if n <= 0:
        list = []
    else:
        if m <= 0:
            for i in range(n):
                list.append(0)
        else:
            number = int(m/n)
            mod = m%n
            for i in range(mod):
                list.append(number+1)
            for j in range(mod,n):
                list.append(number)
    return list            

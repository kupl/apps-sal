def sflpf_data(a, b):
    lis = []
    for i in range(2, b + 1):
        temp = i
        con = 2
        if temp == 1:
            lis.append(1)
        else:
            lis1 = []
            while temp > 1:
                while temp % con == 0:
                    lis1.append(con)
                    temp //= con
                con += 1
                if con * con > temp:
                    if temp > 1:
                        lis1.append(temp)
                    break
            con = lis1[0] + lis1[len(lis1) - 1]
            if con == a and len(lis1) != 1:
                lis.append(i)
    return lis

for i in range(int(input())):
    (n, q) = list(map(int, input().split()))
    dicword = []
    misp = []
    for j in range(n):
        dicword.append(input())
    for j in range(q):
        misp.append(input())
    for j in range(len(misp)):
        temp = misp[j]
        for k in dicword:
            err = 0
            if len(k) == len(temp):
                for l in range(len(temp)):
                    if temp[l] != k[l]:
                        err += 1
                    if err > 1:
                        break
                if err <= 1:
                    print(k)
                    break
            elif len(k) == len(temp) + 1:
                huh = 0
                for l in range(len(temp)):
                    if temp[l] != k[l + huh]:
                        if temp[l] == k[l + 1]:
                            huh += 1
                            err += 1
                        else:
                            err += 1
                    if err > 1 or huh > 1:
                        break
                if err <= 1:
                    print(k)
                    break
            else:
                continue

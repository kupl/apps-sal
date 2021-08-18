try:
    for _ in range(int(input())):
        m, n = map(int, input().split())
        c = []
        last = 0
        flag = True
        rowstart = 0
        rowend = 0
        for i in range(m):
            k = list(input().split())
            co = 0
            k.append(-1)
            k.append(-1)
            for j in range(len(k)):
                if(k[j] == "P"):
                    co += 1
                    if(co == 1):
                        k[-2] = j
                    k[-1] = j
                    rowend = i

            if(k[-1] != -1 and flag):
                flag = False
                rowstart = i
                if(i % 2 == 0):
                    last = k[-2]
                else:
                    last = k[-1]
            c.append(k)
        count = 0

        for i in range(rowstart, rowend + 1):

            if(i % 2 == 0 and c[i][-1] != -1):
                count += abs(last - c[i][-2])
                count += c[i][-1] - c[i][-2]
                last = c[i][-1]
            elif(i % 2 != 0 and c[i][-1] != -1):
                count += abs(last - c[i][-1])
                count += c[i][-1] - c[i][-2]
                last = c[i][-2]
            count += 1
        print(count - 1)


except:
    pass

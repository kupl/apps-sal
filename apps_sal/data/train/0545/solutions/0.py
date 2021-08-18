for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    array = []
    tot = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        aa = temp[0]
        del(temp[0])
        temp.sort()
        temp.insert(0, aa)
        array.append(temp)
    dic = {}
    array.sort(reverse=True)
    for i in array:
        del(i[0])
    for i in range(1, k + 1):
        dic[i] = False
    count = 0
    for i in array:
        count += 1
        for j in i:
            if(dic[j] == True):
                pass
            else:
                tot.append(j)
                dic[j] = True
        if(len(tot) == k):
            break
    if(len(tot) != k):
        print("sad")
    elif(count != n):
        print("some")
    else:
        print("all")

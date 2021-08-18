t = int(input())
L = []
for i in range(t):
    length = int(input())
    s = input()
    x = list(s)
    list_length = int(input())
    l = list(map(int, input().split()))
    for i in range(list_length):
        index = (l[i] - 1) + i
        element = "|"
        x.insert(index, element)
        l1 = []
        for i in range(len(x)):
            if(x[i] == '1'):
                l1.append(i)
        for j in range(len(l1)):
            if(l1[j] == 0 or l1[j] == (len(x) - 1)):
                if(l1[j] == 0 and x[l1[j] + 1] != "|"):
                    x[l1[j] + 1] = "1"
                elif(l1[j] == (len(x) - 1) and x[l1[j] - 1] != "|"):
                    x[l1[j] - 1] = "1"
            else:
                if(x[l1[j] - 1] != "|" and x[l1[j] + 1] != "|"):
                    x[l1[j] - 1] = "1"
                    x[l1[j] + 1] = "1"
                elif(x[l1[j] - 1] != "|" and x[l1[j] + 1] == "|"):
                    x[l1[j] - 1] = "1"
                elif(x[l1[j] - 1] == "|" and x[l1[j] + 1] != "|"):
                    x[l1[j] + 1] = "1"
    num = 0
    for k in range(len(x)):
        if(x[k] == '1'):
            num += 1
    L.append(num)
for m in range(len(L)):
    print(L[m])

t=int(input())
for T in range(0,t):
    n=int(input())
    dict0 = {}
    dict1 = {}
    total = 0
    listset = set()
    for i in range(0,n):
        a,b=map(str,input().split())
        listset.add(a)
        if b == '0':
            if a in dict0 :
                dict0[a] += 1
            else:
                dict0[a] = 1
        else:
            if a in dict1 :
                dict1[a] += 1
            else:
                dict1[a] = 1

    for j in listset:
        if j in dict0 and j in dict1:
            if dict0[j]<dict1[j]:
                total += dict1[j]
            else:
                total += dict0[j]
        elif j in dict0:
            total += dict0[j]
        else:
            total += dict1[j]
    print(total)

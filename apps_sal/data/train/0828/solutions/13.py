# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    l1 = list(map(int, input().split()))
    c = 0
    flag = 0
    for i in range(n):
        if(l1[i] == 0):
            c += 1100
            flag = 1
        elif(l1[i] == 1):
            if(flag == 1):
                c += 100
    print(c)

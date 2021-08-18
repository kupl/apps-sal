n = int(input())
for i in range(n):
    s = int(input())
    k = [int(j) for j in input().split()]
    ss = int(input())
    ks = [int(j) for j in input().split()]
    ki = 0
    j = 0
    while(ki < s and j < ss):
        if(k[ki] == ks[j]):
            j += 1
        ki += 1
    if j == ss:
        print("Yes")
    else:
        print("No")

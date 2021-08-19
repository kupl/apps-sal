# cook your dish here
t = int(input())
for i in range(t):
    D = int(input())
    P = 10**5 - 2
    ans = []
    if(D == 0):
        ans.append(1)
    while(D > 0):
        P = min(P, D)
        ans.append(P + 2)
        ans.append(P + 1)
        ans.append(1)
        D = D - P
    print(len(ans))
    print(*ans, sep=" ", end="\n")

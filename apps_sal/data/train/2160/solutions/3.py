import sys
n,k = list(map(int,input().split()))
l = list(map(int,input().split()))
if sum(l)%k:
    print("No")
else:
    curr = 0
    c = 0
    ans = []
    need = sum(l)//k
    for i in range(n):
        curr += l[i]
        c += 1
        if curr == need:
            ans.append(c)
            curr = 0
            c = 0
        elif curr > need:
            print("No")
            return
    print("Yes")
    print(*ans)


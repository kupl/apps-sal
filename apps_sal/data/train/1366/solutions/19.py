t = int(input())
for z in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    count = 0
    count2 = 0
    for i in L:
        if i == 0:
            count += 1
        else:
            break
    L.reverse()
    for j in L:
        if j == 0:
            count2 += 1
        else:
            break
    ans = n - count - count2
    if ans <= 0:
        ans = 1
    print(ans)

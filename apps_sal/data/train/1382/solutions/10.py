n = int(input())
l = list(map(int, input().split()))
x = int(input())

k = []
for i in l:
    if i < 0:
        k.append(i)

c = len(k)
ans = 0
if c >= x:
    if x == 0:
        print(0)
    else:
        k.sort()
        m = k[x - 1]
        ans += -1 * m * x
        for j in range(len(k)):
            k[j] += -1 * m
        for j in k:
            if j < 0:
                ans += -1 * j
        print(ans)

else:
    ans += -1 * sum(k)
    print(ans)

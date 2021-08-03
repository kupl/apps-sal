t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    ans = 0
    temp = [0] * (m - 1)
    for i in l:
        if i > m:
            ans += 1
        elif i < m:
            temp[i - 1] += 1

    flag = 1
    for i in range(m - 2, -1, -1):
        if temp[i] == 0:
            flag = 0
            break
        else:
            ans += temp[i]
    if flag == 0:
        print("-1")
    else:
        print(ans)

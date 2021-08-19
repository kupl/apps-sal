t = int(input())
for _ in range(t):
    n = int(input())
    flag = 0
    f = [int(x) for x in input().split()]
    for i in range(1, n):
        f[i] += f[i - 1]
    for i in range(0, n):
        if f[i] <= i:
            flag = 1
            break
    if flag == 1:
        print(i)
    else:
        print(f[-1])

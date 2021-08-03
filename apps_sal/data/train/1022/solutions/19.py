t = int(input())
for z in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    flag = 0
    for i in range(n - 2):
        if a[i] != -1 and a[i + 2] != -1 and a[i + 2] != a[i]:
            flag = 1
            break
        elif a[i] != -1 and a[i + 2] == -1:
            a[i + 2] = a[i]
        elif a[i] == -1 and a[i + 2] == -1:
            a[i] = 1
            a[i + 2] = 1
        elif a[i] == -1 and a[i + 2] != -1:
            a[i] = a[i + 2]
    if sum(a) % 2 != 0:
        flag = 1
    if flag == 0:
        print("YES")
        for i in a:
            print(i, end=" ")
        print()
    else:
        print("NO")

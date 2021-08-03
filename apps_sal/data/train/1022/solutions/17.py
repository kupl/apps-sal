t = int(input())
for z in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    flag = 0
    if n % 2 == 0 and (n // 2) % 2 == 0:
        for i in range(n - 2):
            if a[i] != -1 and a[i + n // 2] != -1 and a[i + n // 2] != a[i]:
                flag = 1
                break
            elif a[i] != -1 and a[i + n // 2] == -1:
                a[i + n // 2] = a[i]
            elif a[i] == -1 and a[i + n // 2] == -1:
                a[i] = 1
                a[i + n // 2] = 1
            elif a[i] == -1 and a[i + n // 2] != -1:
                a[i] = a[i + n // 2]
    elif n % 2 == 0:
        k = 1
        for i in a:
            if i != -1:
                k = i
        for i in range(n - n // 2):
            if a[i] != -1 and a[i + n // 2] != -1 and a[i + n // 2] != a[i]:
                flag = 1
                break
            elif a[i] != -1 and a[i + n // 2] == -1:
                a[i + n // 2] = a[i]
            elif a[i] == -1 and a[i + n // 2] == -1:
                a[i] = k
                a[i + n // 2] = k
            elif a[i] == -1 and a[i + n // 2] != -1:
                a[i] = a[i + n // 2]
    else:
        print("NO")
        continue
    if sum(a) % 2 != 0:
        flag = 1
    if flag == 0:
        print("YES")
        for i in a:
            print(i, end=" ")
        print()
    else:
        print("NO")

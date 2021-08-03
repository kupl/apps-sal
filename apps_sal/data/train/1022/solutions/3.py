

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print("NO")
    else:
        b = a[:n // 2]
        c = a[n // 2:]
        flag = True
        for i in range(n // 2):
            if b[i] != -1 and c[i] != -1:
                if b[i] != c[i]:
                    flag = False
                    break
            elif b[i] == -1 and c[i] != -1:
                b[i] = c[i]
            elif b[i] != -1 and c[i] == -1:
                c[i] = b[i]
            else:
                c[i] = 1
                b[i] = 1
        if flag:
            print("YES")
            for x in b:
                print(x, end=' ')
            for x in c:
                print(x, end=' ')
            print()
        else:
            print("NO")

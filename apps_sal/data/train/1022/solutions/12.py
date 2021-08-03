def m(l, n):
    if n % 2 != 0:
        print("NO")
    else:
        c = 0
        for i in range(n // 2):
            if l[i] == l[n // 2 + i]:
                if l[i] == -1:
                    l[i] = 1
                    l[n // 2 + i] = 1
                    continue
                else:
                    continue
            elif l[i] == -1:
                l[i] = l[n // 2 + i]
                continue
            elif l[n // 2 + i] == -1:
                l[n // 2 + i] = l[i]
                continue
            else:
                print("NO")
                c += 1
                break
        if c == 0:
            print("YES")
            print(*l)


t = int(input())
while(t):
    n = int(input())
    l = list(map(int, input().split()))
    m(l, n)
    t -= 1

for i in range(int(input())):
    m = int(input())
    l = []
    p = m ** 2
    ans = 0
    for i in range(1, m + 1):
        if p % i == 0:
            ans += 1
            l.append(i + m)
    print(ans)
    for i in l:
        print(i)

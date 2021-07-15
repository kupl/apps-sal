for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    s = sum(li)
    if s == 0:
        print(1)
    else:
        m = n
        for i in range(n):
            if li[i] == 0:
                m -= 1
            else:
                break
        for i in range(n-1, -1, -1):
            if li[i] == 0:
                m -= 1
            else:
                break
        print(m)

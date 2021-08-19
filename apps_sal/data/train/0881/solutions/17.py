for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    cnt = 0
    for i in range(0, n):
        for j in range(i, n):
            s = x[i:j + 1]
            t = x[i:j + 1]
            s.sort()
            if s == t:
                cnt = cnt + 1
    print(cnt)

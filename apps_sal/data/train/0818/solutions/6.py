t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    p = []
    temp = 0
    for i in range(n):
        if m[i] % 2 == 0:
            m[i] = 0
        else:
            m[i] = 1
        temp = temp + m[i]
        p.append(temp)
    ans = []
    q = int(input())
    for i in range(q):
        (a, b) = list(map(int, input().split()))
        (a, b) = (a - 1, b - 1)
        if a >= 1:
            temp = p[b] - p[a - 1]
        else:
            temp = p[b]
        if temp == b - a + 1:
            print('ODD')
        else:
            print('EVEN')

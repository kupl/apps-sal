# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    m = k
    head = [0] * n
    tail = [0] * n
    head[0] = 0
    tail[-1] = 0
    for i in range(1, n):
        if s[i - 1] == '1':
            head[i] = 1 + head[i - 1]
    for i in range(n - 2, -1, -1):
        if s[i + 1] == '1':
            tail[i] = 1 + tail[i + 1]
    i = 0

    while(i + k <= n):
        c = head[i] + k + tail[i + k - 1]
        m = max(m, c)
        i += 1
    print(m)

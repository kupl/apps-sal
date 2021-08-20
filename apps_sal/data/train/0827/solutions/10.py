t = int(input())
for _1 in range(t):
    (n, k) = map(int, input().split())
    s = input().strip()
    (a, b, ab) = (0, 0, 0)
    for x in range(len(s)):
        if s[x] == 'a':
            a += 1
        if s[x] == 'b':
            b += 1
            ab += a
    print(ab * k + a * b * ((k - 1) * k) // 2)

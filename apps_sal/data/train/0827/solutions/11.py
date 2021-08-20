t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    ans = 0
    total = 0
    b = 0
    s = input()
    for i in range(n):
        if s[i] == 'a':
            ans += 1
        if s[i] == 'b':
            total += ans
            b += 1
    x = b * ans
    sum = 2 * total + (k - 1) * x
    sum = sum * k // 2
    print(sum)

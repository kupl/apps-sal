t = int(input())
while t != 0:
    (x, k) = map(int, input().split())
    cnt = 0
    if k % x == 0:
        a = k / x - 1
    else:
        a = int(k / x)
    for i in range(1, int(a) + 1):
        cnt += x * i
    print(cnt)
    t -= 1

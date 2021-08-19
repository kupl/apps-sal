T = int(input())
for i in range(T):
    (m, n) = map(int, input().split())
    cnt = 0
    a = 10
    while n >= a - 1:
        cnt += 1
        a = a * 10
    ans = m * cnt
    if cnt == 0:
        m = 0
    print(ans, m)

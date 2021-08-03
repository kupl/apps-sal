t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if n < m:
        print(0)
        continue
    dct = dict()

    sum, cnt = 0, 0
    cur = m
    ans = 0
    while cur <= n:
        c = cur % 10
        if c in dct and cur + 10 * m <= n:
            per_sum, per_cnt = sum - dct[c][0], cnt - dct[c][1]
            cycles = (n // m - (cur - 1) // m) // per_cnt
            ans += per_sum * cycles
            cur += cycles * m * per_cnt
        else:
            dct[c] = (sum, cnt)
            ans += c
            cur += m
            sum += c
            cnt += 1
    print(ans)

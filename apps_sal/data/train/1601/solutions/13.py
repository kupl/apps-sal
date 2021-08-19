def R():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    (n, p) = R()
    max_no = n - (int(n / 2) + 1)
    if max_no == 0:
        print(p * p * p)
    else:
        ans = 1 * (p - max_no) * (p - max_no) + (p - n) * (p - max_no) + (p - n) * (p - n)
        print(ans)

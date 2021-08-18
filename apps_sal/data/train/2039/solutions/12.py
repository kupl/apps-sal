def check(M):
    now = 0
    for i in range(n):
        if (now - mas[i]) % m > M:
            if mas[i] > now:
                now = mas[i]
            else:
                return False
    return True


n, m = list(map(int, input().split()))
l = -1
r = m
mas = list(map(int, input().split()))
check(3)
while l < r - 1:
    M = (l + r) // 2
    if check(M):
        r = M
    else:
        l = M
print(r)

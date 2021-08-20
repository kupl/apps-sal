def read():
    return list(map(int, input().split()))


def read_s():
    return list(map(str, input().split()))


(n, m) = read()
ans = 0
while True:
    if n > m:
        ans += m
        n -= 2 * m
    else:
        break
print(ans)

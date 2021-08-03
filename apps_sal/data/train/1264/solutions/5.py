def read(): return list(map(int, input().split()))
def read_s(): return list(map(str, input().split()))


n, m = read()
ans = 0
while n > 0:
    if n > m:
        ans += m
        n -= 2 * m
    else:
        ans += 1
        n -= 2
print(ans)

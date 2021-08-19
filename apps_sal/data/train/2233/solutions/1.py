t = int(input())
a = list(map(int, input().split()))
out = []
for n in a:
    ans = n // 2 + 2
    ans = ans * ans
    ans //= 4
    out.append(ans % 1000000007)
print(' '.join((str(x) for x in out)))

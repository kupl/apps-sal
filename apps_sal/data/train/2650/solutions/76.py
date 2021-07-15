n, l = map(int, input().split())
sl = list(input() for _ in range(n))
sl_s = sorted(sl)

print(*sl_s, sep='')

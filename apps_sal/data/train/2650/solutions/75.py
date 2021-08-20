(n, l) = map(int, input().split())
sl = sorted(list((input() for _ in range(n))))
print(*sl, sep='')

n, l = map(int, input().split())
s = [input() for _ in range(n)]
ans = sorted(s)
print(''.join(ans))

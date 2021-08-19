n = list(map(int, input().split()))[0]
ss = list(sorted([input() for _ in range(n)]))
print(''.join(ss))

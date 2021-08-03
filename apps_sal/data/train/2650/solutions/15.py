n, l = map(int, input().split())
s = [input() for _ in range(n)]
s = sorted(s)

for i in s:
    print(i, end='')

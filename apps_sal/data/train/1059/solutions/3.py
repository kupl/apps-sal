n = int(input())
a = sorted(set([int(input()) for _ in range(n)]))
print(0 if len(a) < 2 else a[-2])

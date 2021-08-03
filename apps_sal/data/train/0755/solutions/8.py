n = int(input())
l = [int(input().strip()) for _ in range(n)]
for k in range(2, max(l)):
    if len(set(e % k for e in l)) == 1:
        print(k, end=' ')

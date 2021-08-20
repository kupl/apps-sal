(N, L) = map(int, input().split())
l = list()
for i in range(N):
    l.append(input())
print(*sorted(l), sep='')

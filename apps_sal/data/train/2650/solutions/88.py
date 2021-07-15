N, L = map(int, input().split())
a = []

for i in range(N):
    a.append(input())

a.sort()

for i in range(N):
    print(a[i],end="")

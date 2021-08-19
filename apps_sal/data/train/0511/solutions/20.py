N = int(input())
a = list(map(int, input().split()))
x = 0
for i in range(N):
    x ^= a[i]
for i in range(N):
    print(x ^ a[i], end=' ')
print()

n = int(input())
j = list(map(int, input().split()))
q = sum(j)
k = 1
for i in range(n - 1):
    x = list(map(int, input().split()))
    y = sum(x)
    if y > q:
        k += 1

print(k)

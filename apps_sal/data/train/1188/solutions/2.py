n = eval(input())
arr = [0 for i in range(n)]
c = list(map(int, input().split()))
for i in range(n):
    if c[i]:
        arr[c[i] - 1] += 1
for i in range(n):
    if arr[i] == 0:
        print(i + 1, end=' ')
print()

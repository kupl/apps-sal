n = int(input())
arr = [(0, 0)] * n
for i in range(n):
    a = sum(list(map(int, input().split())))
    arr[i] = (-a, i)
arr.sort()
for i in range(n):
    if arr[i][1] == 0:
        print(i + 1)

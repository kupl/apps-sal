n = int(input())
arr = sorted([int(a) for a in input().split()])
j = 0
for i in range(0, n):
    if arr[i] > arr[j]:
        j += 1
print(j)



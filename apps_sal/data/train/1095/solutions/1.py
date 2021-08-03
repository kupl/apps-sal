n = int(input())
arr = [int(x) for x in input().split()]
l = [1] * n
if n == 0 or n == 1:
    print('0')
for i in range(0, len(arr)):
    for j in range(i):
        if arr[i] >= arr[j] and l[i] < l[j] + 1:
            l[i] = l[j] + 1

print(n - max(l))

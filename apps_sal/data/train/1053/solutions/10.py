def find(arr, n):
    for i in range(n):
        if arr[i] == 1:
            return i
    return -1


t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    p = find(arr, n)
    if p >= 0:
        print(p)

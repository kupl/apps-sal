# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    arr.sort()
    x = n // 4
    y = 2 * x
    z = 3 * x
    if arr[x] == arr[x - 1] or arr[y] == arr[y - 1] or arr[z] == arr[z - 1]:
        print("-1")
    else:
        print(arr[x], arr[y], arr[z])

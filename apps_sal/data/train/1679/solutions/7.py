# cook your dish here
t = int(input())
while t:
    n, k, x = list(map(int, input().split()))
    arr = [x]
    for i in range(k-1):
        arr.append(0)
    j = 0
    for i in range(n):
        print(arr[j], end = " ")
        j += 1
        if j == k:
            j = 0
    print()
    t -= 1

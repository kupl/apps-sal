for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    for i in range(n):
        res.append(arr[i] + i)
    print(max(res))

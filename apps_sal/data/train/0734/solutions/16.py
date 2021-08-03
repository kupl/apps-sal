t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    arr = []
    mm = 0
    for key, value in d.items():
        mm = max(mm, value)
    for i in range(len(a)):
        arr.append([a[i], i])
    ans = [0] * (n)
    if mm > (n // 2):
        print("No")
    else:
        print("Yes")
        arr = sorted(arr, key=lambda item: item[0])
        for i in range(n):
            ans[arr[(i + mm) % n][1]] = arr[i][0]
        for i in ans:
            print(i, end=" ")
        print()

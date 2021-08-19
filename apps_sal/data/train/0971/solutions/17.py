def changeIt(n, arr):
    m = dict()
    for i in range(n):
        m[arr[i]] = m.get(arr[i], 0) + 1
    count = 0
    for i in m.keys():
        if m[i] > count:
            count = m[i]
        else:
            continue
    print(len(arr) - count)
    return


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    changeIt(n, arr)

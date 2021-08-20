from sys import stdin
input = stdin.readline
t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    arr = []
    for i in range(n):
        (s, f, p) = map(int, input().split())
        arr.append((s, f, p))
    arr.sort(key=lambda x: x[1])
    arr.sort(key=lambda x: x[2])
    i = 0
    j = 0
    cnt = 0
    while i < n:
        if i != 0:
            if arr[i][2] != arr[i - 1][2]:
                cnt = cnt + 1
                j = i
            elif arr[i][0] >= arr[j][1]:
                cnt = cnt + 1
                j = i
        else:
            cnt = cnt + 1
        i = i + 1
    print(cnt)

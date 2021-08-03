# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    maxi = 0
    visited = set()
    count = 0
    sec = -1
    f = 0
    while i < n:
        visited.add(arr[i])
        if len(visited) == 2 and f == 0:
            sec = i
            f = 1
        if len(visited) == k:
            maxi = max(count, maxi)
            count = 1
            i = sec
            visited = {arr[i]}
            f = 0
        else:
            count = count + 1
        i = i + 1
    maxi = max(count, maxi)
    print(maxi)

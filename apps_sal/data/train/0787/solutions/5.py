import sys
for _ in range(int(input())):
    s = str(input())
    arr = [int(i) for i in s]
    n = len(arr)
    total = 0
    cnt = 0
    lstindx, curr = n - 1, n - 1
    while arr[curr] == 1 and curr >= 0:
        curr -= 1
        lstindx -= 1
    while curr >= 0:
        if arr[curr] == 1:
            if arr[curr + 1] == 0:
                cnt += 1
            total += cnt + (lstindx - curr)
            lstindx -= 1
        curr -= 1
    print(total)

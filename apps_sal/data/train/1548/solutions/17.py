t = int(input())
for t1 in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    left = []
    right = []
    for i in range(0, n):
        if i == 0:
            left.append((a[i], i))
        else:
            if a[i] < (left[-1][0] + left[-1][1] + 1):
                left.append((a[i], 0))
            else:
                left.append((left[-1][0], left[-1][1] + 1))

    right = []
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            right.append((a[i], 0))
        else:
            if a[i] < (right[-1][0] + right[-1][1] + 1):
                right.append((a[i], 0))
            else:
                right.append((right[-1][0], right[-1][1] + 1))
    ans = []
    right = right[::-1]
    for i in range(0, n):
        ans.append(min(left[i][0] + left[i][1], right[i][0] + right[i][1]))
    print(*ans)

t = int(input())
for t1 in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    left = []
    right = []
    for i in range(0, n):
        if i == 0:
            left.append((a[i], i))
        elif a[i] < left[-1][0] + left[-1][1] + 1:
            left.append((a[i], 0))
        else:
            left.append((left[-1][0], left[-1][1] + 1))
    right = []
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            right.append((a[i], 0))
        elif a[i] < right[-1][0] + right[-1][1] + 1:
            right.append((a[i], 0))
        else:
            right.append((right[-1][0], right[-1][1] + 1))
    right = right[::-1]
    final1 = []
    for i in range(0, n):
        final1.append(min(left[i][0] + left[i][1], a[i]))
    final2 = []
    for i in range(0, n):
        final2.append(min(right[i][0] + right[i][1], a[i]))
    ans = []
    for i in range(0, n):
        ans.append(min(final1[i], final2[i]))
    print(*ans)
    'l=a[::]\n    for i in range(1,n):\n     a[i]=min(a[i],a[i-1]+1)\n\n    for i in range(n-2,-1,-1):\n     a[i]=min(a[i+1]+1,a[i])\n\n    if a!=ans:\n     print(l)\n     print(a)\n     #print(left)\n     #print(right)\n     print(ans)\n     print()\n    print(a)\n    print()\n    for i in range(1,n):\n     a[i]=min(a[i],a[i-1]+1)\n\n    for i in range(n-2,-1,-1):\n     a[i]=min(a[i+1]+1,a[i])\n    print(*a)'

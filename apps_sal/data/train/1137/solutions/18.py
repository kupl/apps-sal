for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    (l, r) = (0, n - 1)
    ans = 'Rejected'
    while l < r:
        k = arr[l] + arr[r]
        if k == 2000:
            ans = 'Accepted'
            break
        elif k > 2000:
            r -= 1
        else:
            l += 1
    print(ans)

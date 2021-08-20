t = int(eval(input('')))
for i in range(t):
    (n, k) = [int(n) for n in input(' ').split()]
    lst = list(map(int, input().split()))
    j = 0
    leftover = 0
    ans = 0
    for i in range(n):
        j = lst[i] + leftover
        leftover = j - k
        if j < k:
            ans = i + 1
            break
    if leftover >= 0:
        ans = n + leftover // k + 1
    print(ans)

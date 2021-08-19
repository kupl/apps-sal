for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
        continue
    seq = list(map(int, input().split()))
    (pref, suff) = (0, n - 1)
    for i in range(1, n):
        if seq[i] > seq[i - 1]:
            pref = i
        else:
            break
    for i in range(n - 2, -1, -1):
        if seq[i] < seq[i + 1]:
            suff = i
        else:
            break
    (l, r, ans) = (0, suff, 0)
    while r < n and l <= pref:
        if seq[l] < seq[r]:
            ans += n - r
            l += 1
        else:
            r += 1
    if suff < pref:
        print(n * (n + 1) // 2 - 1)
        continue
    print(ans + (pref + 1) + (n - suff))

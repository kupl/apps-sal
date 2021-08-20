t = int(input())
for _ in range(t):
    finalans = 0
    n = int(input())
    seq = list(map(int, input().split()))
    (ans, r, count, i) = (1, 0, 0, 1)
    while i < n:
        tem = i + r
        if seq[i] >= seq[i - 1] and tem % 2 == 1 or (seq[i] <= seq[i - 1] and tem % 2 == 0):
            ans += 1
            if i == n - 1 and count < 1:
                ans += 1
        elif seq[i] >= seq[i - 1] and tem % 2 == 0:
            if count < 1:
                ref = i - 1
                ans += 2
                r += 1
                count = 1
            else:
                finalans = max(ans, finalans)
                ans = i - ref
                r = ref % 2
                i -= 1
                count = 0
        elif seq[i] <= seq[i - 1] and tem % 2 == 1:
            if count < 1:
                ref = i
                ans += 2
                r += 1
                count = 1
            else:
                finalans = max(ans, finalans)
                ans = i - ref
                r = ref % 2
                i -= 1
                count = 0
        i += 1
    finalans = max(finalans, ans)
    print(finalans)

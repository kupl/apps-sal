(n, k) = list(map(int, input().split()))
(a, ans, count) = (list(map(int, input().split())), 0, 0)
a.sort()
for x in a:
    if ans + x <= k:
        ans += x
        count += 1
    else:
        break
print(count)

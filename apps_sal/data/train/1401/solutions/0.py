(n, k) = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
(sum, cnt) = (0, 0)
for price in prices:
    sum += price
    if sum <= k:
        cnt += 1
    else:
        break
print(cnt)

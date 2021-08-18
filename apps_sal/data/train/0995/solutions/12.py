r = int(input())
arr = [int(i) for i in input().split()]
k = int(input())
maxi = 0
for x in range(k):
    k1 = x
    k2 = k - x
    summation = sum(arr[:k1]) + (sum(arr[-k2:]) if k2 > 0 else 0)
    maxi = max(summation, maxi)

print(maxi)

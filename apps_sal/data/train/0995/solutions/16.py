r = int(input())
arr = [int(i) for i in input().split()]
k = int(input())
maxi = 0
for x in range(k):
    k1 = x
    k2 = k - x
    s1 = sum(arr[:k1]) + (sum(arr[-k2:]) if k2 > 0 else 0)
    s2 = sum(arr[:k2]) + (sum(arr[-k1:]) if k1 > 0 else 0)
    summation = max(s1, s2)
    maxi = max(summation, maxi)

print(maxi)

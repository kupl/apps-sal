import collections
(n, p, k) = map(int, input().split())
arr = list(map(int, input().split()))
dic = collections.defaultdict(int)
for i in range(n):
    tmp = arr[i] ** 4 - arr[i] * k
    tmp %= p
    dic[tmp] += 1
ans = 0
for key in dic.keys():
    ans += dic[key] * (dic[key] - 1) // 2
print(ans)

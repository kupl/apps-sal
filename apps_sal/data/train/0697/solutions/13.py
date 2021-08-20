t = int(input())
ans = []
for _ in range(t):
    (n, k) = [int(x) for x in input().split(' ')]
    arr = [int(x) for x in input().split(' ')]
    curr = sum(arr[0:k])
    best = curr
    for i in range(n - k):
        curr = curr - arr[i] + arr[i + k]
        if curr > best:
            best = curr
    ans.append(best)
for i in ans:
    print(i)

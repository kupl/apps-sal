from sys import stdin

# Input data
#stdin = open("input", "r")


for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    arr = list(map(int, stdin.readline().split()))
    ans = sum(arr[:k])
    s = sum(arr[:k])
    for i in range(k, n):
        s += arr[i]
        s -= arr[i - k]
        ans = max(ans, s)
    print(ans)


import sys
sys.setrecursionlimit(10000000)


def prime(n):
    ans = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            temp1 = 1
            while n % i == 0:
                n //= i
                temp1 *= i
            ans.append(temp1)
        i += 1
    if n > 1:
        ans.append(n)
    return ans


def recur(arr, k):
    if len(arr) == k:
        return sum(arr)
    ans = float('inf')
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            temp = arr[:]
            temp.remove(arr[i])
            temp.remove(arr[j])
            temp.append(arr[i] * arr[j])
            ans = min(ans, recur(temp, k))
    return ans


tc = int(input())
for i in range(tc):
    (k, x) = list(map(int, input().split()))
    p = prime(x)
    if len(p) <= k:
        print(sum(p) + k - len(p))
    else:
        print(recur(p, k))

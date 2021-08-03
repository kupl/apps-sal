# cook your dish here
import sys
sys.setrecursionlimit(10000000)


def primes(x):
    f = []
    i = 2
    while i * i <= x:
        if x % i == 0:
            t = 1
            while x % i == 0:
                x //= i
                t *= i
            f.append(t)
        i += 1
    if x > 1:
        f.append(x)
    return f


def recur(arr):
    if len(arr) == k:
        return sum(arr)
    answer = float('inf')
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            temp = arr[:]
            temp.remove(arr[i])
            temp.remove(arr[j])
            temp.append(arr[i] * arr[j])
            answer = min(answer, recur(temp))
    return answer


for _ in range(int(input())):
    k, X = map(int, input().split())
    p = primes(X)
    if k >= len(p):
        print(sum(p) + (k - len(p)))
        continue
    print(recur(p))

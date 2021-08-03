input()

k = min(map(int, input().split()))

n = int(input())

p = sorted(map(int, input().split()), reverse=True) + [0] * k

print(sum(sum(p[i: i + k]) for i in range(0, n, k + 2)))

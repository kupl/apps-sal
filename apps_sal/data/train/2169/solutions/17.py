from collections import defaultdict

n, p, k = map(int, input().split())
keys = list(map(int, input().split()))
dictionary = defaultdict(lambda: 0)
answer = 0

for key in keys:
    answer += dictionary[(key ** 4 - k * key) % p]
    dictionary[(key ** 4 - k * key) % p] += 1

print(answer)

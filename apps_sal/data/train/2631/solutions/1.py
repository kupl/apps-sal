from itertools import product
(K, M) = list(map(int, input().split()))
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = [sum((i ** 2 for i in x)) % M for x in product(*N)]
print(max(results))

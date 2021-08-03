from itertools import permutations
for _ in range(int(input())):
    pick = 0
    n, q = map(int, input().split(' '))
    print(round((q * (n + q + 1) / (q + 1)), 10))

import random
(n, m, c) = list(map(int, input().split()))
print(3)
for i in range(n):
    for j in range(m):
        print(random.randint(1, 50), end=' ')
    print('')

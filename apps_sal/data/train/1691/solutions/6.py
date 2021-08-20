import random
(n, m, c) = list(map(int, input().split()))
print(3)
for i in range(n):
    for j in range(m):
        while True:
            l = random.randint(1, 50)
            h = random.randint(1, 50)
            if l < h:
                break
        print(random.randint(l, h), end=' ')
    print('')

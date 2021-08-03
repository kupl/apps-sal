import random
n, m, c = list(map(int, input().split()))
print(3)
for i in range(n):
    for j in range(m):
        l = random.randint(1, 7)
        h = random.randint(7, 50)
        print(random.randint(l, h), end=' ')
    print("")

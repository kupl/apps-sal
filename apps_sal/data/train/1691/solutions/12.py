import random
n, m, c = list(map(int, input().split()))
print(3)
for i in range(n):
    for j in range(m):
        l = random.randint(1, 10)
        h = random.randint(11, 50)
        print(random.randint(l, h), end=' ')
    print("")

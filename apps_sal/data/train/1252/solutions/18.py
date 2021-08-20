n = 1000001
sieve = [0] * (n + 1)
sieve[0] = 1
sieve[1] = 1
for x in range(2, n + 1):
    if sieve[x]:
        continue
    for u in range(2 * x, n + 1, x):
        sieve[u] = 1
for i in range(int(input())):
    n = int(input())
    count = 0
    sum1 = 0
    for i in range(n + 1):
        if sieve[i] == 0:
            sum1 += i
    print(sum1 % 10)

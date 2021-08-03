sieve = [False] + [True] * 10000
s = []
for x in range(2, 10001):
    if(sieve[x]):
        s.append(x)
        for i in range(2 * x, 10001, x):
            sieve[i] = False
cnt = [0] * (10001)
n = 10000
for x in s:
    for y in s:
        if(x + 2 * y) > n:
            break
        cnt[x + 2 * y] += 1
for _ in range(int(input())):
    n = int(input())
    print(cnt[n])

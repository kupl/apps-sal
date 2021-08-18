isPrime = [1 for i in range(10001)]
cnt = [0 for i in range(10001)]
isPrime[0] = 0
isPrime[1] = 0
prime = []
for i in range(2, 10001):
    if isPrime[i]:
        prime.append(i)
        for j in range(i * i, 10001, i):
            isPrime[j] = 0
for i in prime:
    for j in prime:
        if (i + 2 * j) > 10000:
            break
        else:
            cnt[i + 2 * j] += 1
for _ in range(int(input())):
    n = int(input())
    print(cnt[n])

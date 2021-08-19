n = int(input())
primes = [2]
primes_bool = [2 for _ in range(10 ** 5 + 4)]
primes_bool[2] = 1
for i in range(3, 10 ** 5 + 4, 2):
    isPrime = True
    for j in range(len(primes)):
        if primes[j] ** 2 > i:
            break
        if i % primes[j] == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
        primes_bool[i] = 1
if n <= 2:
    print(1)
else:
    print(2)
print(*primes_bool[2:n + 2])

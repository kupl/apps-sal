def isprime(n):
    if n <= 3:
        return 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    else:
        return 1


t = int(input())
for i in range(t):
    (x, y) = map(int, input().split())
    z = x + y + 1
    while isprime(z) != 1:
        z += 1
    print(z - (x + y))

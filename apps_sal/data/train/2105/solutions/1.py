def isprime(n):
    if n == 2:
        return 1
    else:
        for i in range(2, int(n**0.5) + 2):
            if n % i == 0:
                return 0
        return 1


n = int(input())
if n <= 2:
    print(1)
    for i in range(n):
        print(1, end=' ')
else:
    print(2)
    for i in range(2, n + 2):
        if isprime(i):
            print(1, end=' ')
        else:
            print(2, end=' ')


def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]

    p = 2
    while(p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    sum = 0

    for p in range(2, n + 1):
        if prime[p]:
            sum += p
    return sum


x = int(input())
for i in range(0, x):
    uptil = int(input())
    sum = SieveOfEratosthenes(uptil)
    print(sum % 10)

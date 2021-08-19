import math
import array


def is_prime(x):
    i = 2
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i = i + 1
    return True


prime = [False for c in range(1000)]
n = int(input())
i = 2
answer = 0
while i <= n:
    if prime[i - 1] == True:
        i = i + 1
        continue
    if is_prime(i):
        answer = answer + 1
        prime[i - 1] = True
        j = i * i
        while j <= n:
            prime[j - 1] = True
            answer = answer + 1
            j = j * i
    i = i + 1
i = 2
print(answer)
while i <= n:
    if prime[i - 1]:
        print(i, end=' ')
    i = i + 1

from math import sqrt


def prime_facs(n):
    l = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            l.append(i)
    return l


for a0 in range(int(input())):
    n = int(input())
    x = prime_facs(n ** 2)
    print(len(x))
    for i in x:
        print(i + n)

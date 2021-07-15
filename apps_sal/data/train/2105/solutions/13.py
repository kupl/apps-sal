from math import sqrt

def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

prime_lst = []
n = int(input())

if n < 3:
    print(1)
else:
    print(2)
for i in range(2, n+2):
    if prime(i):
        print(1, end=" ")
    else:
        print(2, end=" ")


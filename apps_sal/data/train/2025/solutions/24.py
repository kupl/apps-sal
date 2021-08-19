n = int(input())


def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


l = []
for i in range(2, n + 1):
    if isprime(i) == True:
        l.append(i)
l2 = []
for i in l:
    c = 1
    while i ** c <= n:
        l2.append(i ** c)
        c += 1
print(len(l2))
for i in l2:
    print(i, end=' ')

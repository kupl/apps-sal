from math import factorial

t = int(input())

for i in range(t):

    s = input()
    hash = {}

    for j in s:
        try:
            hash[j]
        except:
            hash[j] = 1
        else:
            hash[j] += 1
    z = factorial(len(s))
    m = 10**9 + 7
    k = 1

    for j in list(hash.keys()):
        k *= factorial(hash[j])
    print((z // k) % m)

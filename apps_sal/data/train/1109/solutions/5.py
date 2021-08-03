from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


t = eval(input())
while(t):
    leng = 0
    t = t - 1
    m = eval(input())
    leng = len(factors(m))
    if(leng % 2):
        print("YES")
    else:
        print("NO")

# cook your dish here
from math import sqrt


def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True


def psum(n):
    a = []
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            if prime(i):
                a.append(i)
    if prime(n):
        a.append(n)
    return sum(a)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    k = 0
    while(l < len(a)):
        for i in range(len(a)):
            if i != l:
                if a[i] % a[l] == 0:
                    # print(a[i]," ",a[l])
                    if psum(a[i]) % psum(a[l]) == 0:
                        k += 1
        l += 1
    print(k)

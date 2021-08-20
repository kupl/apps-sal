import sys
m = 1000000007


def dcexpo(b, p):
    if p == 0:
        return 1
    temp = dcexpo(b, p >> 1)
    temp = temp ** 2
    if p & 1:
        temp = temp * b
    return temp % m


t = int(input())
for test in range(t):
    k = int(input())
    ret = dcexpo(3, k)
    if k & 1:
        ret -= 3
    else:
        ret += 3
    print(ret)

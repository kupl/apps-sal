import sys


def input():
    return sys.stdin.readline().rstrip('\r\n')


a = [0] * 10 ** 5
for i in range(len(a)):
    a[i] = a[i - 1] + i * i
for _ in range(int(input())):
    k = int(input())
    print(a[k - 1])

mod = 1000000007


def ii():
    return int(input())


def si():
    return input()


def dgl():
    return list(map(int, input()))


def f():
    return map(int, input().split())


def il():
    return list(map(int, input().split()))


def it():
    return tuple(map(int, input().split()))


def ls():
    return list(input())


t = ii()
for _ in range(t):
    n = ii()
    l = il()
    mn = l[-1]
    c = 0
    for i in range(n - 1, -1, -1):
        if l[i] > mn:
            c += 1
        mn = min(mn, l[i])
    print(c)

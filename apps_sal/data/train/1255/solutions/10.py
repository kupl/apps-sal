from math import sqrt


def ii():
    return int(input())


def si():
    return input()


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


abc = 'abcdefghijklmnopqrstuvwxyz'
t = ii()
while t:
    t -= 1
    m = [0] * 26
    s = input().split()
    s1 = s[0]
    k = int(s[1])
    n = len(s1)
    for i in range(len(s1)):
        m[ord(s1[i]) - ord('a')] += 1
    s = ''
    for i in range(26):
        if m[i] != 0:
            if k > 0:
                s += abc[i]
                k -= 1
        else:
            s += abc[i]
    if n != len(s[:n]):
        print('NOPE')
    else:
        print(s[:n])

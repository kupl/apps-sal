def listLCM(l):
    ans = 1
    for i in l:
        ans = lcm(ans, i)
    return ans


def lcm(a, b):
    return (a * b) / gcd(a, b)


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


tc = int(input())
for _ in range(tc):
    people = int(input())
    candidates = list(set(map(int, input().split())))
    resh = int(input())
    print(int(listLCM(candidates)) + resh, end=' ')

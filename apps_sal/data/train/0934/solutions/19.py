m = 1000000007


def value(a, b, c):
    return (a + b) * (b + c) % m


t = int(input())
while t:
    t -= 1
    sum = 0
    (p, q, r) = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    if min(a) > max(b) or max(b) < min(c):
        sum = 0
    else:
        for i in b:
            for j in a:
                for k in c:
                    if j <= i and i >= k:
                        sum = sum % m + value(j, i, k)
    print(sum % m)

m = 1000000007


def value(a, b, c):
    return (a + b) * (b + c)


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
            if i >= min(a) and i >= min(c):
                for j in a:
                    if j <= i:
                        for k in c:
                            if i >= k:
                                sum = sum + value(j, i, k)
        'for i in b:\n            if i>=min(a) and i>=min(c):\n                a1 = [j for j in a if j<=i]\n                c1 = [j for j in c if j<=i]\n                for j in a1:\n                    for k in c1:\n                        #if j<=i and i>=k:\n                        sum = sum + value(j,i,k)'
    print(sum % m)

def num(l):
    ans = 0
    for i in range(len(l)):
        ans = ans * 10 + l[i]
    return ans


def numof(n):
    ans = 0
    l = []
    while n > 0:
        l.append(n % 10)
        n = n // 10
        ans += 1
    l.reverse()
    return l


t = int(input())
for you in range(t):
    n = int(input())
    done = 0
    z = numof(n)
    l = []
    for i in range(len(z)):
        if min(z[i:]) == z[i]:
            l.append(z[i])
        else:
            l.append(min(z[i:]))
            done = 1
            break
    k = len(l)
    for i in range(len(z) - k):
        l.append(9)
    print(num(l))

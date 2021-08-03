t = int(input())


def power(a, n):
    ans = 1
    for i in range(n):
        ans *= a
    return ans


for i in range(t):
    k = int(input())
    print(10 * (power(2, (k - 1))))

mo = 10 ** 9 + 7


def findNumbers(n, w):
    x = 0
    s = 0
    if w >= 0 and w <= 8:
        x = 9 - w
    elif w >= -9 and w <= -1:
        x = 10 + w
    s = pow(10, n - 2, mo)
    s *= x % mo
    return s % mo


for i in range(int(input())):
    (n, w) = map(int, input().split())
    print(findNumbers(n, w))

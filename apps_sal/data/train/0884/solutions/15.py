from numpy import array
t = int(input())


def factor(n):
    l = []
    for i in range(2, n + 1):
        if n % i == 0:
            l.append(i)
    return l


while t > 0:
    x, k = list(map(int, input().split(" ")))
    xF = factor(x)
    kF = factor(k)

    arr1 = array(xF)
    arr2 = array(kF)
    xS = arr1**array([k] * len(xF))
    kS = arr2 * array([x] * len(kF))
    print(sum(xS), sum(kS))
    t -= 1

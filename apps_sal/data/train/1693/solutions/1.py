import sys


def uniform_variance(mean):
    return (2 * mean) ** 2 / 12

def poisson_variance(mean):
    mean = sum(a) / len(a)
    return mean

def dist(a):
    mean = sum(a) / len(a)
    var = 0
    for k in a:
        var += (mean - k) ** 2

    var /= len(a)

    uniform = abs(uniform_variance(mean) - var)
    poisson = abs(poisson_variance(mean) - var)

    if uniform > poisson:
        return 'poisson'
    else:
        return 'uniform'



n = int(sys.stdin.readline())
for i in range(n):
    a = [int(x) for x in sys.stdin.readline().split()]
    print(dist(a))



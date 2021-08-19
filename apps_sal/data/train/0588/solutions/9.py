# cut pizza codechef solution
# first try to handle boundary conditions, if n(cuts) = 360, return 0
from math import gcd
from functools import reduce


def n_cuts(x):
    """
       x: list of cuts 

       """
    l = len(x)
    if(l == 360):
        print(0)
        return

    # find minimum difference
    mini = min(x)
    flag = 0
    for i in range(len(x)):
        if(x[i] % mini != 0):
            flag = 1
            break
    if(flag == 0):
        if(360 % mini == 0):
            print(360 // mini - l)
            return

    # find gcd
    GCD = reduce(gcd, x)
    result = int(360 / GCD)
    print(result - l)
    return


def __starting_point():
    t = int(input())  # number of test cases
    for i in range(t):
        n = int(input())  # not use
        x = list(map(int, input().split(' ')))  # x is the cuts list
        diff = []
        for i in range(1, len(x)):
            diff.append(x[i] - x[i - 1])
        diff.append(360 - x[-1] + x[0])
        n_cuts(diff)


__starting_point()

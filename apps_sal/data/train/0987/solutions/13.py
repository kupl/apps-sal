import math


def func():
    t = int(input())
    for _ in range(t):
        (fn, dst, ta, bs) = map(int, input().split(' '))
        t1 = fn / bs
        t2 = math.sqrt(2 * (fn + dst) / ta)
        if t1 < t2:
            print('Bolt')
        else:
            print('Tiger')


func()

import numpy
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = numpy.prod(a)
    if s % 2 == 0:
        print('NO')
    else:
        print('YES')

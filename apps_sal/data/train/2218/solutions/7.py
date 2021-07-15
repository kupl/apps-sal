
# -*- coding: utf-8 -*-
# @Date    : 2019-08-01 06:48:30
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb = RI()
have = RMI()
nb_ops = RI()

curr = [-1] * nb
maxs = 0

ops = [RMI() for _ in range(nb_ops)][::-1]
for i in ops:
    if i[0] == 2:
        maxs = max(maxs, i[1])
    else:        
        if curr[i[1] - 1] == -1:
            curr[i[1] - 1] = max(maxs, i[2])
for i in range(nb)            :
    if curr[i] == -1:
        curr[i] = max(maxs, have[i])


print(*curr)

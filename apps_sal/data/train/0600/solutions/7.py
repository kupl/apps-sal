import math


def r(n):
    cycle = 60
    index = (1 << int(math.floor(math.log2(n)))) % cycle
    cur = 0
    next = 1
    for i in range(1, index):
        nextNext = (cur + next) % 10
        cur = next
        next = nextNext
    return cur


t = int(input())
for i in range(t):
    c = int(input())
    print(r(c))

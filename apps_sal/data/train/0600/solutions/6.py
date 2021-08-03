import math


def r(n):
    cycle = 60
    index = (1 << len(bin(n)) - 3) % cycle
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

import sys
import math


def test_case():
    N, K, x, y = [int(i) for i in input().split()]
    dir_x = 1
    dir_y = 1
    while K > 0:
        K -= 1
        dis_x = (N - x * (dir_x)) % N
        dis_y = (N - y * (dir_y)) % N

        if dis_x == 0:
            dis_x = N
        if dis_y == 0:
            dis_y = N
        if dis_x == dis_y:
            K = 0
        dis = min(dis_x, dis_y)
        x += dis * dir_x
        y += dis * dir_y
        if dis_x < dis_y:
            dir_x *= -1
        else:
            dir_y *= -1
    print(x, y)


T = int(input())
for _ in range(0, T):
    test_case()

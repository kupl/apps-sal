import math
import sys
import time


def getLevel(number):
    _level = math.floor(math.log(number, 2))
    return int(_level)


def isPair(number):
    return number % 2 == 0


def getInterval(a, b, max):
    _max = max
    _loop = -1
    _apart = 0
    while _apart == 0 and _max != 1:
        _loop += 1
        _max = _max >> 1
        if a < _max and b >= _max:
            _apart = 1
        elif a >= _max:
            a = a - _max
            b = b - _max
    return _loop


def resolve2(nodes):
    if nodes[0] == nodes[1]:
        return 0
    l = 0
    k = 0
    while nodes[0] != nodes[1]:
        if nodes[1] < nodes[0]:
            if nodes[0] > 1:
                nodes[0] = nodes[0] / 2 if isPair(nodes[0]) else (nodes[0] - 1) / 2
                l += 1
        elif nodes[1] > 1:
            nodes[1] = nodes[1] / 2 if isPair(nodes[1]) else (nodes[1] - 1) / 2
            k += 1
    return l + k


def __starting_point():
    step = 0
    for line in sys.stdin:
        if step == 0:
            step = 1
            continue
        nodes = [int(nums) for nums in line.strip().split()]
        if nodes[0] == nodes[1]:
            print(0)
            continue
        _temp = nodes[0]
        if nodes[0] < nodes[1]:
            nodes[0] = nodes[1]
            nodes[1] = _temp
        _max_level = getLevel(nodes[0])
        if nodes[1] == 1:
            print(_max_level)
            continue
        _min_level = getLevel(nodes[1])
        substract = _max_level - _min_level
        if substract != 0:
            nodes[0] = nodes[0] >> substract
        _temp = nodes[0]
        if nodes[0] < nodes[1]:
            nodes[0] = nodes[1]
            nodes[1] = _temp
        if nodes[1] == nodes[0]:
            print(substract)
            continue
        _max = 2 ** _min_level
        apart = getInterval(nodes[1] - _max, nodes[0] - _max, _max)
        print(2 * (_min_level - apart) + substract)


__starting_point()

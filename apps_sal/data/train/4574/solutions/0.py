# -*- coding: utf-8 -*-
def build_a_wall(x=0, y=0):
    if type(x) != int or type(y) != int or x < 1 or y < 1:
        return
    if x * y > 10000:
        return "Naah, too much...here's my resignation."
    res = [["■■"] * y if i & 1 ^ x & 1 else ["■"] + ["■■"] * (y - 1) + ["■"] for i in range(x)]
    return '\n'.join(map('|'.join, res))

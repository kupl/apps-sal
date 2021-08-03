from time import struct_time as st, mktime as mk


def past(h, m, s):
    return int(mk(st((2020, 1, 2, h, m, s, 3, 4, 5))) -
               mk(st((2020, 1, 2, 0, 0, 0, 3, 4, 5)))) \
        * 1000

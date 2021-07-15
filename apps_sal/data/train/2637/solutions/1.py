#!/usr/bin/env python3

from math import atan
from math import degrees

def __starting_point():
    ab = int(input().strip())
    bc = int(input().strip())
    
    print("{}°".format(int(round(degrees(atan(ab/bc))))))
__starting_point()

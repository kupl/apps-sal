#!/usr/bin/env python3

import re

def __starting_point():
    t = int(input().strip())
    
    for _ in range(t):
        try:
            re.compile(input().strip())
            res = True
        except BaseException:
            res = False
        print(res)
__starting_point()

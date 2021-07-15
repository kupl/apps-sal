#!/usr/bin/env python3

import string
symbols = string.ascii_lowercase

from itertools import combinations

def __starting_point():
    n = int(input().strip())
    arr = list(map(str, input().strip().split(' ')))
    times = int(input().strip())
    cmbts = list(combinations(sorted(arr), times))
    
    print(("{:.4f}".format(len(list([a for a in cmbts if a[0] == 'a']))/(len(cmbts)))))
    

__starting_point()
